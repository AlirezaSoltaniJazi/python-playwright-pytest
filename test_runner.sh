python -m pytest tests \
  -v \
  --setup-show \
  --headed \
  --slowmo 1000 \
  -m "login" \
  --html=./report/html/report.html \
  -n auto
