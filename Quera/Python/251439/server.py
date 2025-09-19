import pickle
import threading
from typing import List, Callable


class OlympicsServer:
    def __init__(self):
        self.lock = threading.Lock()
        self.subscribers: dict[str, List[Callable]] = dict()
        self.messages = self._load_messages()

    def publish(self, topic: str, message: str, qos: int):
        with self.lock:
            matched_subscribers = []
            for sub_topic, callbacks in self.subscribers.items():
                if self._is_topic_matched(sub_topic, topic):
                    matched_subscribers.extend(callbacks)

            if qos == 1 and not matched_subscribers:
                self._store_message(topic, message)

            for callback in matched_subscribers:
                threading.Thread(target=callback, args=(topic, message)).start()

    def subscribe(self, topic: str, callback: Callable):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []

            self.subscribers[topic].append(callback)

            self._deliver_stored_messages(topic, callback)

    def _is_topic_matched(self, sub_topic: str, pub_topic: str):
        sub_levels = sub_topic.split('/')
        pub_levels = pub_topic.split('/')

        for i, sub_level in enumerate(sub_levels):
            if sub_level == '#':
                return True
            elif sub_level == '+':
                continue
            elif i >= len(pub_levels):
                return False
            elif sub_level != pub_levels[i]:
                return False

        return len(sub_levels) == len(pub_levels)

    def _load_messages(self):
        try:
            with open('messages.pkl', 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def _store_message(self, topic: str, message: str):
        self.messages.append((topic, message))

        with open('messages.pkl', 'wb') as f:
            pickle.dump(self.messages, f)

    def _deliver_stored_messages(self, topic: str, callback: Callable):
        for stored_topic, stored_message in self.messages:
            if self._is_topic_matched(topic, stored_topic):
                threading.Thread(target=callback, args=(stored_topic, stored_message)).start()
