#filename:client.py (in chap10)
#function: client in MQTT IOT protocol

MQTTv31 = 3
class Client(object):

    def __init__(self, client_id="", clean_session=True, userdata=None, protocol=MQTTv31):
        
        print("Client contructor")
        if not clean_session and (client_id == "" or client_id is None):
            raise ValueError('A client id must be provided.')

        self._protocol = protocol
        self._userdata = userdata
        self._sock = None
        self._sockpairR, self._sockpairW = _socketpair_compat()
        self._keepalive = 60
        self._message_retry = 20
        self._last_retry_check = 0
        self._clean_session = clean_session
        if client_id == "" or client_id is None:
            self._client_id = "paho/" + "".join(random.choice("0123456789ADCDEF") for x in range(23-5))
        else:
            self._client_id = client_id

        self._username = ""
        self._password = ""
        self.on_message = None
        
        
        self._will_topic = ""
        self._will_payload = None
        self._will_qos = 0
        self._will_retain = False
       
