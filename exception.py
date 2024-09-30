import sys

class customexception(Exception):
    
    def __init__(self, error_message, error_details:sys):
        self.error_messgae=error_message
        _,_,exc_tb=error_details.exc.info()
        print(exc_tb)
        
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "Error Occured in python script name [{0}] line number [{1}] error message[{2}]".format(self.file_name, self.lineno, str(self.error_messgae))
     
     
if __name__=="__main__":
    try:
        a=1/0
        
    except Exception as e:
        raise customexception(e, sys)
