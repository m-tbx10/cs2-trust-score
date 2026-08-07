def output_convention(success: bool, steam_id, error_code: str, error_msg: str) -> dict:
    if success == True:
        return {
            "success": success, 
            "steam_id": steam_id, 
            "error": None
        }
    else:
        return {
            "success": success, 
            "steam_id": steam_id, 
            "error": {
                "code": error_code,
                "message": error_msg
            }
        }
