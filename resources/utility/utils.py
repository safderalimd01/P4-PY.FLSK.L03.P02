def api_failure(error):
    respone =  {
		"api_call_status": {
			"Message": error,
			"Status": "Failure"
		}
	}, 400
    return respone


def api_success(rowncols, message):
	respone = dict()

	respone["api_call_status"] = {
		"Message": message,
		"Status": "Success"
	}

	if isinstance(rowncols, list) or isinstance(rowncols, dict):
		respone["sproc_output_result"] = rowncols
	return respone, 200

def close_connection(conn, cursor):
	cursor.close()
	conn.close()
