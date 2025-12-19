import sys
def get_error_message(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error_message = "Error happens in File [{0}] at line number [{1}] and the Error is [{2}]".format(
        fileName,lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
