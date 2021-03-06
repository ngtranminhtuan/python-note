watchmedo auto-restart --directory . \
                        --ignore-pattern='*/call_tasks.py' \
                        --pattern '*.py' \
                        --recursive \
                        -- celery worker \
                            -A tasks_sample \
                            --loglevel=info \
                            --concurrency=3 \
                            -n worker1@%h \
                            -Q queue1,queue2

# NOTE: nếu chỉ định queue khi chạy worker thì lúc call task cũng phải chỉ định queue
# nếu không task sẽ không chạy                            
