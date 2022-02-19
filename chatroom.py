import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    if rc == 0: 
        client.connected_flag=True
        print("Connected")
    else:
        print("Bad Connection ",rc)
        
def on_message(client,userdata,message):
    print("message.topic ",message.topic)
    if str(message.topic)!=pubtop:
        print(str(message.topic), str(message.payload.decode("utf-8")))
        
def on_subscribe(client,userdata,mid,granted_qos):
    print("Subscribed ",str(mid), str(granted_qos))

def on_disconnect(client,userdata,rc):
    if rc!=0:
        print("Unexpectd disconnection")


broker_addr="test.mosquitto.org"
port=1883

client=mqtt.Client()

client.on_connect=on_connect
client.on_message=on_message
client.on_subscribe=on_subscribe


client.connect(broker_addr,port)

pubtop=input("Topic to be published")
subtop=input("Topic to be subscribed")

client.loop_start()
client.subscribe(subtop)

while(1):
    user=input()
    if(user=='exit'):
        break
    elif(user=='subscribe'):
        new_subtop=input('Subscribe to topic ?')
        client.subscribe(new_subtop)
    elif(user=='publish'):
        pubtop=input('publish the topic')
    else:
        client.publish(pubtop,user)
        
client.disconnect()
client.loop_stop()







