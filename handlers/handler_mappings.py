from handlers.message_handlers import hello
from handlers.message_handlers import goodbye


MESSAGE_MAPPINGS = {
    "hello": hello.cmd,
    "goodbye": goodbye.cmd,
}
