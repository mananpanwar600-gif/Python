'''
Garbage collection is a memory management technique used in programming languages to automatically reclaim memory that is no longer accessible or in use by the application. To handle such circular references, Python uses a Garbage Collector (GC) from the built-in gc module. This collector is able to detect and clean up objects involved in reference cycles.
'''

import gc
## enable the garbage collection

gc.enable()
gc.disable()
gc.collect()


## get garbage collection stats

print(gc.get_stats())

## get unreachable objects

print(gc.garbage)