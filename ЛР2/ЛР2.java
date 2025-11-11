//Мультисписок(вложенный список)

import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) {
        List<List<Integer>> multilist = new ArrayList<>();
        multilist.add(List.of(1, 2, 3));
        multilist.add(List.of(4, 5, 6));
        multilist.add(List.of(7, 8, 9));
    }
}

//Очередь

import java.util.LinkedList;
import java.util.Queue;
public class QueueExample {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();
        queue.offer("A"); 
        queue.offer("B");  
        queue.offer("C");
    }
}

//Дек

import java.util.Deque;
import java.util.ArrayDeque;
public class DequeExample {
    public static void main(String[] args) {
        Deque<Integer> deq = new ArrayDeque<>();
        deq.offerLast(1);  
        deq.offerFirst(2); 
        deq.offerLast(3); 
    }
}

//Приоритетная очередь

import java.util.PriorityQueue;
public class PriorityQueueExample {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(10);
        pq.offer(20);
        pq.offer(5);
    }
}

//Приоритетная очередь с компаратором:

Comparator<Task> idComparator = Comparator.comparing(Task::id);
PriorityQueue<Task> priorityQueue = new PriorityQueue<>(idComparator);
priorityQueue.add(new Task(10001, "Task 1", 5));
priorityQueue.add(new Task(10003, "Task 3", 10));
priorityQueue.add(new Task(10002, "Task 2", 1));
