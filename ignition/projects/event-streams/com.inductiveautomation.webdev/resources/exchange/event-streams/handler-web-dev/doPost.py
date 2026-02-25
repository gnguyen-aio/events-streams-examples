def doPost(request, session):
	logger = system.util.getLogger("HTTP Handler | handler-web-dev Web Dev Resource")
	data = request['data']
	message = "My Message: " + str(data)
	logger.info(message)
	request['servletResponse'].setStatus(200)
	return {'response':message}