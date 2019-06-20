.PHONY: setup

setup:
	@echo "Settuping up radicale..."
	cd radicale && ./setup.sh
	@echo "Setting up postgres..."
	docker-compose run --rm --entrypoint bash agendav -c "cd /var/www/agendav && ./agendavcli migrations:migrate -n"

up:
	docker-compose down
	docker-compose build
	docker-compose up
