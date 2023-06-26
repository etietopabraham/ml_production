import sys

def get_exception(error, error_detail:sys)->str:
    _,_,exc_tb = error_detail.exc_info()
    error_message = "An error has occured in file [{0}], at line [{1}], error details is [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = get_exception(error=error_message, error_detail=error_details)

    def __str__(self) -> str:
        return self.error_message

# Test
#import logger
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logger.logging.info("divide by zero exception")
#         raise CustomException(e, sys)
