from typing import Generic, List, Optional, Set, TypeVar
import heapq

T = TypeVar('T')

class MinHeap(Generic[T]):
    __heap: List[T]
    __heap_items: Set[T]

    def __init__(self, heap: Optional[List] = None) -> None:
        self.__heap_items = set()

        if heap:
            self.__heap = heap
            heapq.heapify(self.__heap)
            for item in heap:
                self.__heap_items.add(item)
        else:
            self.__heap = []

    def insert(self, item: T) -> None:
        if item not in self.__heap_items:
            self.__heap_items.add(item)
            heapq.heappush(self.__heap, item)

    def extract_min(self) -> T:
        item = heapq.heappop(self.__heap)
        self.__heap_items.remove(item)
        return item

    def empty(self) -> bool:
        return not self.__heap_items

    def __contains__(self, item: T) -> bool:
        return item is not None and item in self.__heap_items

    def __getitem__(self, key: int) -> T:
        return self.__heap[key]

    def __setitem__(self, key: int, value: T) -> None:
        if self.__heap[key] == value:
            return

        self.__heap_items.remove(self.__heap[key])
        self.__heap[key] = value
        self.__heap_items.add(value)
        heapq.heapify(self.__heap)
