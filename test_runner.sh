python -m pytest tests \
  -v \
  --setup-show \
  --headed \
  --slowmo 1000 \
  -m "search" \
  --html=./report/html/$(date +%Y-%m-%d-%H-%M-%S)/report.html \
  -n auto \
  --screenshot on --output=./report/playwright/$(date +%Y-%m-%d-%H-%M-%S)/ \
  --video on --output=./report/playwright/$(date +%Y-%m-%d-%H-%M-%S)/
  #  --screenshot only-on-failure
  #  --browser chromium --device "iPhone 11"
  #  --browser-channel msedge
  #  --browser-channel chrome \
  #  --browser chromium --browser firefox --browser webkit
