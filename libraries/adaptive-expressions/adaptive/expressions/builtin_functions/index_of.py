from ..expression_evaluator import ExpressionEvaluator
from ..expression_type import INDEXOF
from ..function_utils import FunctionUtils
from ..return_type import ReturnType
from ..options import Options


class IndexOf(ExpressionEvaluator):
    def __init__(self):
        super().__init__(
            INDEXOF, IndexOf.evaluator, ReturnType.Number, IndexOf.validator
        )

    @staticmethod
    def evaluator(expression: object, state, options: Options):
        result = -1
        args, error = FunctionUtils.evaluate_children(expression, state, options)
        if error is None:
            if isinstance(args[0], str) or args[0] is None:
                if isinstance(args[1], str) or args[1] is None:
                    result = str(args[0]).find(args[1])
                else:
                    error = "Can only look for indexof string in " + expression.to_string()
            elif isinstance(args[0], list):
                for i, arg in enumerate(list(args[0])):
                    if args[1] == arg:
                        result = i
                        break
            else:
                error = "{" + expression.to_string() + "} works only on string or list."
        return result, error

    @staticmethod
    def validator(expression: object):
        FunctionUtils.validator_order(expression, None, [ReturnType.Array | ReturnType.String, ReturnType.Object])
