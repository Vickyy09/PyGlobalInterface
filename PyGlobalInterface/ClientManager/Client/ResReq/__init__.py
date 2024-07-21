from PyGlobalInterface.log import configure_logger

logger = configure_logger(__name__)
class Events:
    AWK_CLIENT_RECV = "AWK_CLIENT_RECV"
    
    AWK_CLIENT_VERIFY = "AWK_CLIENT_VERIFY"
    AWK_CLIENT_NOT_VERIFY_DUE_TO_CHECK = "AWK_CLIENT_NOT_VERIFY_DUE_CHECK"
    AWK_CLIENT_NOT_VERIFY_DUE_TO_LIMIT = "AWK_CLIENT_NOT_VERIFY_DUE_TO_LIMIT"


    AWK_CLIENT_FUNCTION_CALL = "AWK_CLIENT_FUNCTION_CALL"
    AWK_CLIENT_FUNCTION_CALL_ERROR = "AWK_CLIENT_FUNCTION_CALL_ERROR"

    AWK_CLIENT_FUNCTION_RETURN = "AWK_CLIENT_FUNTION_RETURN"
    AWK_CLIENT_FUNCTION_RETURN_ERROR = "AWK_CLIENT_FUNCTION_RETURN_ERROR"

    SERVER_REQ_CLIENT_TELEMETRY="SERVER_REQ_CLIENT_TELEMETRY"
    SERVER_REQ_CLIENT_SHUTDOWN="SERVER_REQ_CLIENT_SHUTDOWN"

    REQ_VERIFY = "REQ_VERIFY"
    REQ_FUNCTION_CALL = "REQ_FUNCTION_CALL"
    REQ_FUNCTION_RETURN = "REQ_FUNCTION_RETURN"
    REQ_GOING_SHUTDOWN = "REQ_GOING_SHUTDOWN"

class EventsClientManger:
    REQ_MAKE_CLIENT_VERIFY = "REQ_MAKE_CLIENT_VERIFY"
    AWK_MAKE_CLIENT_VERIFY_SUC = "AWK_MAKE_CLIENT_VERIFY_SUC"
    AWK_MAKE_CLIENT_VERIFY_ERR = "AWK_MAKE_CLIENT_VERIFY_ERR"

    REQ_MAKE_FUNCTION_CALL = "REQ_MAKE_FUNCTION_CALL"
    AWK_MAKE_FUNCTION_CALL_SUC = "AWK_MAKE_FUNCTION_CALL_SUC"
    AWK_MAKE_FUNCTION_CALL_ERR = "AWK_MAKE_FUNCTION_CALL_ERR"

    REQ_MAKE_FUNCTION_RET = "REQ_MAKE_FUNCTION_RET"
    AWK_MAKE_FUNCTION_RET_SUC = "AWK_MAKE_FUNCTION_RET_SUC"
    AWK_MAKE_FUNCTION_RET_ERR = "AWK_MAKE_FUNCTION_RET_ERR"

class ClientManagerEvents:
    FUNCTION_CALL = "FUNCTION_CALL"
    CLIENT_ERROR = "CLIENT_ERROR"
    CLIENT_VERIFYED = "CLIENT_VERIFYED"
    

class ClientEvents:
    AWK = "AWK"
    
    REQ_REGISTER = "REQ_REGISTER"
    REGISTER_GRANTED = "REGISTER_GRANTED"
    REGISTER_FAIL = "REGISTER_FAIL"

    REQ_FUNCTION_REGISTER = "REQ_FUNCTION_REGISTER"
    FUNCTION_REGISTER_SUCCESFUL = "FUNCTION_REGISTER_SUCCESFUL"
    FUNCTION_REGISTER_FAIL = "FUNCTION_REGISTER_FAIL"


    REQ_FUNCTION_CALL = "REQ_FUNCTION_CALL"
    FUNCTION_CALL_SUCCESFUL = "FUNCTION_CALL_SUCCESFUL"
    FUNCTION_CALL_FAIL = "FUNCTION_CALL_FAIL"

    SFUNCTION_RETURN = "SFUNCTION_RETURN"
    SEFUNCTION_RETURN = "SEFUNCTION_RETURN"
    
    RFUNCTION_RETURN = "RFUNCTION_RETURN"
    REFUNCTION_RETURN = "REFUNCTION_RETURN"

    REQ_CLOSE ="REQ_CLOSE"

