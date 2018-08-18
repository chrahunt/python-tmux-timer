# tmux timer

This package provides a timer that can be used in tmux.

## Usage

First, set up your tmux config to run the display command

```
set -g status-right '#(tmux_timer show)'
```

Next, set up bindings to invoke the timer

```
bind t run-shell "tmux_timer toggle"
```
