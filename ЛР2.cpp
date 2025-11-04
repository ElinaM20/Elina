//Мультисписок(вложенный список)

#include <iostream>
#include <vector>
int main() {
    std::vector<std::vector<int>> multilist = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
}

//Очередь

#include <iostream>
#include <queue>
int main() {
    std::queue<int> q;
    q.push(1);
    q.push(2);
}

//Дек

#include <iostream>
#include <deque>
int main() {
    std::deque<int> deq;
    deq.push_back(1);  
    deq.push_front(2); 
    deq.push_back(3);
}

//Приоритетная очередь с примитивным типом

#include <iostream>
#include <queue>
int main() {
    std::priority_queue<int> pq;
    pq.push(10); 
    pq.push(20); 
    pq.push(5);  
}

//Приоритетная очередь с пользовательской структурой

#include <iostream>
#include <queue>
#include <string>
struct Task {
 std::string name;
 int priority;
 bool operator<(const Task& other) const {
 return priority < other.priority;
 }
};
int main() {
 std::priority_queue<Task> taskQueue;
 taskQueue.push({"Task 1", 2});
 taskQueue.push({"Task 2", 1});
 taskQueue.push({"Task 3", 3});
}
