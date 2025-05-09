from typing import Dict, List, Any, Optional
import autogen
import logging
import json
from autogen import Agent, AssistantAgent


class EvaluationWorkflow:
    def __init__(self, team: Dict[str, Agent], log_level: int = logging.INFO):
        """
        初始化测评工作流

        Args:
            team: 包含所有评测智能体的agent字典
            log_level: 日志级别
        """
        # 验证团队必须包含协调者和用户代理
        if "coordinator" not in team or "user_proxy" not in team:
            raise ValueError("团队必须包含'coordinator'和'user_proxy'智能体")

        self.team = team
        self.coordinator = team["coordinator"]
        self.user_proxy = team["user_proxy"]

        # 设置日志
        self.logger = self._setup_logger(log_level)

        # 注册智能体之间的连接关系
        self._register_agent_connections()

        self.logger.info("评测工作流初始化完成")

    def _setup_logger(self, log_level: int) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger(f"{__name__}.{id(self)}")
        logger.setLevel(log_level)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def _register_agent_connections(self):
        """注册智能体连接（100%兼容AutoGen参数传递）"""
        # 协调者与专家连接
        for agent_name, agent in self.team.items():
            if agent_name not in ["coordinator", "user_proxy"]:
                self.coordinator.register_reply(
                    agent,
                    lambda *args, **kwargs: (False, None)  # 同时接受位置和关键字参数
                )
                agent.register_reply(
                    self.coordinator,
                    lambda *args, **kwargs: (False, None)
                )
                self.logger.debug(f"已建立连接: coordinator <-> {agent_name}")

        # 用户代理与协调者连接
        self.user_proxy.register_reply(
            self.coordinator,
            lambda *args, **kwargs: (False, None)
        )
        self.coordinator.register_reply(
            self.user_proxy,
            lambda *args, **kwargs: (False, None)
        )
        self.logger.debug("已建立连接: user_proxy <-> coordinator")

    def run_evaluation(self, content_to_evaluate: str, max_turns: int = 1):
        """单次评测入口"""
        try:
            chat_result = self.user_proxy.initiate_chat(
                recipient=self.coordinator,
                message=f"请直接返回JSON格式评测结果：\n{content_to_evaluate}",
                max_turns=1
            )

            # 尝试提取JSON
            try:
                return self._extract_json_from_last_message()
            except Exception as e:
                return {
                    "error": f"结果解析失败: {str(e)}",
                    "raw_response": str(chat_result)
                }

        except Exception as e:
            return {"error": f"评测流程错误: {str(e)}"}

    def _extract_json_from_last_message(self):
        """新版消息提取方法"""
        try:
            chat_history = self.coordinator.chat_messages.get(self.user_proxy, [])
            if not chat_history:
                raise ValueError("没有对话记录")

            last_msg = chat_history[-1]["content"]
            # 这里放你原来的JSON提取逻辑（正则表达式等）
            return json.loads(last_msg.split("```json")[1].split("```")[0])
        except Exception as e:
            raise ValueError(f"JSON提取失败: {str(e)}")

        # 如果无法提取JSON，返回原始消息
        return {"message": last_message}