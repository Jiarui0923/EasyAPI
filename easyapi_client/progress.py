import time
import sys

class LoadProgress(object):
    def __init__(self, desc='', timer=False):
        self._desc = desc
        self._markers = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self._marker_iter = iter(self._markers)
        self._this_marker = 0
        self._time_start = time.perf_counter()
        self._timer = timer
        self.show()
    def update(self, desc=None, marker=None):
        self._desc = self._desc if desc is None else desc
        self._this_marker = (self._this_marker + 1) % len(self._markers)
        self.show(marker=marker)
    def _build_time(self, seconds):
        if seconds < 60: return f'{seconds:.1f}s'
        elif seconds >= 60 and seconds <= 3600: return f'{int(seconds/60)}m{seconds%60:.1f}s'
        else: f'{int(seconds/3600)}h{int(seconds/60)}m{seconds%60:.1f}s'
    def show(self, marker=None):
        _marker = self._markers[self._this_marker] if marker is None else marker
        if self._timer:
            _time_used = self._build_time(time.perf_counter()-self._time_start)
            sys.stdout.write(f'\r[{_time_used}] {_marker} {self._desc}')
        else:
            sys.stdout.write(f'\r{_marker} {self._desc}')
        sys.stdout.flush()
    def done(self, desc=None):
        self.update(desc=desc, marker='✓')
    def error(self, desc=None):
        self.update(desc=desc, marker='✗')