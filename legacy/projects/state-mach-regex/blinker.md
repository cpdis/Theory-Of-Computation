# Blinker State Machine

_Draw out the state machine for a car's turn signal system. What are the
transitions leading to both lights not blinking, one light blinking, the other light blinking, or both lights blinking?_

## States

- **Off** --> Both blinkers are turned off
- **Left** --> Left blinker is turned on (right blinker is turned off)
- **Right** --> Right blinker is turned on (left blinker is turned off)
- **Both** --> Both blinkers are turned on (i.e. hazard lights on)

## Transitions

- **Up**: Pull the turn signal up to turn right
- **Down**: Push the turn signal down to turn left
- **Neutral**: Put the turn signal in the middle (neutral position)
- **Hazard On**: Push the button to turn the hazard signal on
- **Hazard Off**: Push the button to turn th hazard signal off
