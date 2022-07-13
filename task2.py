# coding: utf-8
# !/usr/bin/env python2.7


class BufferFifo:
    def __init__(self, size_array):
        self.size_array = size_array
        self.buffer_array = []

    def adding(self, data_array):
        for el in data_array:
            self.buffer_array.append(el)
            if len(self.buffer_array) > self.size_array:
                self.buffer_array.pop(0)

    def get(self, count_elements):
        res = []
        for i in range(count_elements):
            if len(self.buffer_array) >= 1:
                res.append(self.buffer_array.pop(0))
            else:
                print 'Buffer is empty!'
                return res

        return res

    def clear(self):
        self.buffer_array = []
        print 'Buffer array is clear.'


fifo = BufferFifo(10)

print 'buffer =', fifo.buffer_array
fifo.adding([12, 2, 4, 67, 8, 9, 23, 8, 10, 33])
print 'buffer =', fifo.buffer_array
fifo.clear()
fifo.adding([11, 0, 0, 0, 3])
print 'buffer =', fifo.buffer_array
fifo.adding([12, 4, 67, 8, 9, 23, 10, 33])
print 'buffer =', fifo.buffer_array
print fifo.get(5), '<--- get_elements'
print 'buffer =', fifo.buffer_array
print fifo.get(15), '<--- get_elements'
print 'buffer =', fifo.buffer_array
print


class HoldBufferFifo:
    def __init__(self, size_array):
        self.size_array = size_array
        self.buffer_array = []

    def adding(self, data_array):
        for el in data_array:
            if len(self.buffer_array) < self.size_array:
                self.buffer_array.append(el)
            else:
                print 'Buffer is full! Buffer = ', self.buffer_array
                break

    def get(self, count_elements):
        res = []
        for i in range(count_elements):
            if len(self.buffer_array) >= 1:
                res.append(self.buffer_array.pop(0))
            else:
                print 'Buffer is empty!'
                return res

        return res

    def clear(self):
        self.buffer_array = []
        print 'Buffer array is clear.'


fifo = HoldBufferFifo(10)

print 'buffer =', fifo.buffer_array
fifo.adding([12, 2, 4, 67, 8, 9, 23, 8, 10, 33])
print 'buffer =', fifo.buffer_array
fifo.clear()
fifo.adding([11, 0, 0, 0, 3])
print 'buffer =', fifo.buffer_array
fifo.adding([12, 4, 67, 8, 9, 23, 10, 33])
print 'buffer =', fifo.buffer_array
print fifo.get(5), '<--- get_elements'
print 'buffer =', fifo.buffer_array
print fifo.get(15), '<--- get_elements'
print 'buffer =', fifo.buffer_array
