from ex30 import SocketFSM


def test_basic_connection():
    fsm = SocketFSM()
    script = ["connect", "accept", "read", "read", "write", "close", "connect"]

    for event in script:
        print(event, ">>>", fsm)
        fsm.handle(event)

test_basic_connection()
