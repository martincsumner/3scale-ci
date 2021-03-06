swagger: '2.0'
info:
  x-threescale-system-name: 'echo-api'
  title: 'Echo API'
  version: '1.0'
host: 'echo-api.3scale.net'
paths:
  /:
    get:
      operationId: Echo
      summary: 'Get an echo'
      description: 'Get an echo from the server'
      x-threescale-smoketests-operation: true
      responses:
        200:
          description: 'An Echo from the server'
security:
- apikey: []
securityDefinitions:
  apikey:
    name: api-key
    in: header
    type: apiKey
