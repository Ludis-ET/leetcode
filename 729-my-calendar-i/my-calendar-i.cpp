class MyCalendar {
public:
    MyCalendar() {}

    multiset<pair<int, int>>ml;
    bool book(int start, int end) 
    {
        auto it = ml.lower_bound({end, 0});

        if(it != ml.begin())
        {
            auto prev = it;
            prev--;
            if(prev->first > start) return false;
        }
        if(it != ml.end() and it->second < end) return false;
        ml.insert({end, start});
        return true;
    }
};