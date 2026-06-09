from __future__ import annotations

import logging

from src.agentforge.core.completion.completion_manager import CompletionManager
from src.agentforge.core.events.event_bus import Event, EventBus
from src.agentforge.core.runtime.execution_context import ExecutionContext
from src.agentforge.core.task.task import Task
from src.agentforge.infrastructure.providers.base_provider import BaseProvider
from src.agentforge.infrastructure.providers.provider_models import (
    ProviderRequest,
    Message,
    MessageRole,
)

logger = logging.getLogger(__name__)


class AgentRuntime:
    def __init__(
        self,
        provider: BaseProvider,
        completion_manager: CompletionManager,
        event_bus: EventBus,
    ) -> None:
        self.provider = provider
        self.completion_manager = completion_manager
        self.event_bus = event_bus

    async def execute(self, task: Task, model_name: str = "default-model") -> Task:
        context = ExecutionContext(
            task=task, provider_name=self.provider.provider_name, model_name=model_name
        )

        self.event_bus.publish(
            Event(event_type="task_started", payload={"task_id": str(task.task_id)})
        )

        try:
            request_message_content = (
                task.description if task.description else task.title
            )

            request = ProviderRequest(
                task_id=task.task_id,
                execution_id=context.execution_id,
                messages=[
                    Message(role=MessageRole.USER, content=request_message_content)
                ],
                model=model_name,
                system_prompt="You are a helpful AI assistant.",
            )

            response = await self.provider.generate(request)

            if not self.completion_manager.validate(response):
                raise ValueError("Invalid response from provider")

            self.completion_manager.complete(task, response)

            self.event_bus.publish(
                Event(
                    event_type="task_completed", payload={"task_id": str(task.task_id)}
                )
            )

        except Exception as e:
            logger.error(f"Runtime execution failed for task {task.task_id}:{e}")

            self.completion_manager.fail(task, error=e)

            self.event_bus.publish(
                Event(
                    event_type="task_failed",
                    payload={"task_id": str(task.task_id), "error": str(e)},
                )
            )

        return task
