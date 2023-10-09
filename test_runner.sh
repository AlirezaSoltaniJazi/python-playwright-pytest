python -m pytest tests \
  -v \
  --setup-show \
  --headed \
  --slowmo 5000 \
  -m "search" \
  --html=./report/html/report.html \
  -n auto
