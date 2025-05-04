"""
简化版评测入口
用户只需要传入评测内容
"""
import json
import logging
from typing import Dict, Any

from workflow import EvaluationWorkflow
from agents import EvaluationAgentFactory
from config import DEEPSEEK_API_CONFIG, MODEL_CONFIG, EVALUATION_CONFIG

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("evaluation")


def evaluate(content: str) -> Dict[str, Any]:
    """
    评测函数 - 只需传入内容

    Args:
        content: 要评测的直播内容

    Returns:
        评测结果
    """
    try:


        # 创建智能体
        factory = EvaluationAgentFactory()

        # 创建所有必要的智能体
        coordinator = factory.create_coordinator_agent()
        accuracy_expert = factory.create_accuracy_agent()
        comprehensiveness_expert = factory.create_comprehensiveness_agent()
        logic_expert = factory.create_logic_agent()
        professionalism_expert = factory.create_professionalism_agent()
        totalscore_expert = factory.create_totalscore_agent()
        user_proxy = factory.create_user_proxy()



        # 组装团队
        team = {
            "coordinator": coordinator,
            "accuracy_expert": accuracy_expert,
            "comprehensiveness_expert": comprehensiveness_expert,
            "logic_expert": logic_expert,
            "professionalism_expert": professionalism_expert,
            "totalscore_expert": totalscore_expert,
            "user_proxy": user_proxy
        }

        # 执行评测
        workflow = EvaluationWorkflow(team)
        result = workflow.run_evaluation(
            content_to_evaluate=content,
            max_turns=EVALUATION_CONFIG["max_turns"]
        )

        return result

    except Exception as e:
        logger.exception("评测过程出错")
        return {"error": str(e)}


def main():
    """
    主函数 - 简化版，只接收内容参数
    """
    import sys

    # 检查是否提供了内容
    if len(sys.argv) < 2:
        print("用法: python main.py <评测内容>")
        return

    # 获取评测内容
    content = sys.argv[1]

    # 执行评测
    result = evaluate(content)

    # 打印结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()