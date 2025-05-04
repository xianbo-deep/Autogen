import autogen
from typing import Dict, List, Any, Optional
from config import MODEL_CONFIG

class EvaluationAgentFactory:
    """智能体工厂类，负责创建和配置评测所需的各种智能体"""

    @staticmethod
    def create_coordinator_agent(name: str = "Coordinator"):
        """创建协调者智能体，负责整体评测流程的协调和结果汇总"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是直播评测系统的协调者。你负责:
            1. 协调各专家智能体进行评测工作
            2. 收集并整合所有维度的评测结果
            3. 生成最终的JSON格式评测报告
            4. 确保评测流程的完整性和一致性

            必须严格按照以下JSON格式返回最终结果：

            {
              "metrics": [
                {
                  "metricId": "accuracy",
                  "metricname": "准确性",
                  "score": 85.5,
                  "description": {
                    "level": "优秀",
                    "suggestion": "建议xxx",
                    "evaluation": "评估结论xxx"
                  }
                },
                {
                  "metricId": "comprehensiveness",
                  "metricname": "全面性",
                  "score": 80.0,
                  "description": {
                    "level": "良好",
                    "suggestion": "建议xxx",
                    "evaluation": "评估结论xxx"
                  }
                },
                {
                  "metricId": "logic",
                  "metricname": "逻辑性",
                  "score": 90.0,
                  "description": {
                    "level": "优秀",
                    "suggestion": "建议xxx",
                    "evaluation": "评估结论xxx"
                  }
                },
                {
                  "metricId": "professionalism",
                  "metricname": "专业性",
                  "score": 75.5,
                  "description": {
                    "level": "良好",
                    "suggestion": "建议xxx",
                    "evaluation": "评估结论xxx"
                  }
                }
              ],
              "totalscore": [
                {
                  "score": 82.75
                }
              ]
            }

            注意：
            - 所有评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求
            - 总分应该是所有指标分数的平均值""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_accuracy_agent(name: str = "AccuracyExpert"):
        """创建准确性评测专家智能体"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是专注于评估直播内容准确性的专家。你需要:
            1. 检查直播中陈述的事实是否准确
            2. 识别任何错误信息或误导性内容
            3. 评估信息来源的可靠性
            4. 给出1-100的准确性评分
            5. 必须严格按照以下JSON格式返回结果：

            {
              "metrics": [
                {
                  "metricId": "accuracy",
                  "metricname": "准确性",
                  "score": 85.5,  // 这里是1-100之间的分数值
                  "description": {
                    "level": "优秀",  // 等级评估，如"优秀"、"良好"、"一般"、"需改进"等
                    "suggestion": "建议xxx",  // 改进建议
                    "evaluation": "评估结论xxx"  // 详细评估
                  }
                }
              ]
            }

            注意：
            - 评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_comprehensiveness_agent(name: str = "ComprehensivenessExpert"):
        """创建全面性评测专家智能体"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是专注于评估直播内容全面性的专家。你需要:
            1. 评估直播是否涵盖了主题的所有关键方面
            2. 检查是否有重要信息被遗漏
            3. 评估内容的深度和广度
            4. 给出1-100的全面性评分
            5. 必须严格按照以下JSON格式返回结果：

            {
              "metrics": [
                {
                  "metricId": "comprehensiveness",
                  "metricname": "全面性",
                  "score": 85.5,  // 这里是1-100之间的分数值
                  "description": {
                    "level": "优秀",  // 等级评估，如"优秀"、"良好"、"一般"、"需改进"等
                    "suggestion": "建议xxx",  // 改进建议
                    "evaluation": "评估结论xxx"  // 详细评估
                  }
                }
              ]
            }

            注意：
            - 评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_logic_agent(name: str = "LogicExpert"):
        """创建逻辑性评测专家智能体"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是专注于评估直播内容逻辑性的专家。你需要:
            1. 分析论点的结构和推理过程
            2. 识别任何逻辑谬误或矛盾
            3. 评估结论是否由前提合理推导出
            4. 检查内容组织的连贯性和清晰度
            5. 给出1-100的逻辑性评分
            6. 必须严格按照以下JSON格式返回结果：

            {
              "metrics": [
                {
                  "metricId": "logic",
                  "metricname": "逻辑性",
                  "score": 85.5,  // 这里是1-100之间的分数值
                  "description": {
                    "level": "优秀",  // 等级评估，如"优秀"、"良好"、"一般"、"需改进"等
                    "suggestion": "建议xxx",  // 改进建议
                    "evaluation": "评估结论xxx"  // 详细评估
                  }
                }
              ]
            }

            注意：
            - 评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_professionalism_agent(name: str = "ProfessionalismExpert"):
        """创建专业性评测专家智能体"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是专注于评估直播内容专业性的专家。你需要:
            1. 评估主持人/讲者的专业知识水平
            2. 检查专业术语的使用是否恰当
            3. 评估内容的深度和技术准确性
            4. 考量信息的时效性和相关性
            5. 给出1-100的专业性评分
            6. 必须严格按照以下JSON格式返回结果：

            {
              "metrics": [
                {
                  "metricId": "professionalism",
                  "metricname": "专业性",
                  "score": 85.5,  // 这里是1-100之间的分数值
                  "description": {
                    "level": "优秀",  // 等级评估，如"优秀"、"良好"、"一般"、"需改进"等
                    "suggestion": "建议xxx",  // 改进建议
                    "evaluation": "评估结论xxx"  // 详细评估
                  }
                }
              ]
            }

            注意：
            - 评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_totalscore_agent(name: str = "TotalScoreExpert"):
        """创建总体评价专家智能体"""
        return autogen.AssistantAgent(
            name=name,
            system_message="""你是专注于根据专业性、逻辑性、全面性、准确性给出全面评价的专家。你需要:
            1. 综合评估主持人/主播的整体表现
            2. 给出1-100分的总分
            3. 必须严格按照以下JSON格式返回结果：

            {
              "totalscore": [
                {
                  "score": 85.5  // 这里是1-100之间的分数值
                }
              ]
            }

            注意：
            - 评分必须是double类型数值
            - 不要添加任何额外的字段
            - 确保JSON格式完全符合要求""",
            llm_config=MODEL_CONFIG
        )

    @staticmethod
    def create_user_proxy(name: str = "UserProxy"):
        """创建用户代理智能体，负责提供直播内容并接收评测结果"""
        return autogen.UserProxyAgent(
            name=name,
            human_input_mode="NEVER",
            is_termination_msg=lambda msg: "EVALUATION_COMPLETE" in msg.get("content", ""),
            code_execution_config=False
        )


def create_evaluation_team() -> Dict[str, Any]:
    """创建完整的评测团队"""
    factory = EvaluationAgentFactory()

    team = {
        "coordinator": factory.create_coordinator_agent(),
        "accuracy_expert": factory.create_accuracy_agent(),
        "comprehensiveness_expert": factory.create_comprehensiveness_agent(),
        "logic_expert": factory.create_logic_agent(),
        "professionalism_expert": factory.create_professionalism_agent(),
        "totalscore_expert": factory.create_totalscore_agent(),
        "user_proxy": factory.create_user_proxy()
    }

    return team


def get_evaluation_result_schema() -> Dict[str, Any]:
    """返回评测结果的JSON架构"""
    return {
        "metrics": [
            {
                "bsonType": "array",
                "description": "评估指标列表",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "metricId": {
                            "bsonType": "string",
                            "description": "指标 ID"
                        },
                        "metricname": {
                            "bsonType": "string",
                            "description": "指标名称"
                        },
                        "score": {
                            "bsonType": "double",
                            "description": "分数"
                        },
                        "description": {
                            "bsonType": "object",
                            "description": "描述信息",
                            "properties": {
                                "level": {
                                    "bsonType": "string",
                                    "description": "评估等级"
                                },
                                "suggestion": {
                                    "bsonType": "string",
                                    "description": "改进建议"
                                },
                                "evaluation": {
                                    "bsonType": "string",
                                    "description": "评估结论"
                                }
                            }
                        }
                    }
                }
            }
        ],
        "totalscore": [
            {
                "score": {
                    "bsonType": "double",
                    "description": "总分分数"
                }
            }
        ]
    }