class MyQueue {
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        if (s2.size() == 0){
            while (s1.size() != 0){
                s2.push(s1.top());
                s1.pop();
            }
        }

        if (s2.size() == 0){
            return -1; 
            // or raise an error; 
        }
        int top = s2.top();
        s2.pop();
        return top;


    }
    
    int peek() {
        if (s2.size() == 0){
            while (s1.size() != 0){
                s2.push(s1.top());
                s1.pop();
            }
        }

        if (s2.size() == 0){
            return -1; 
            // or raise an error; 
        }
        int top = s2.top();
        return top;
    }
    
    bool empty() {
        return s1.size() == 0 && s2.size() == 0;
    }

private:
    std::stack<int> s1;
    std::stack<int> s2;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */