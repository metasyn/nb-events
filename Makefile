.PHONY: setup

setup:
	@echo "Settuping up radicale..."
	cd radicale && ./setup.sh
	@echo "Setting up postgres..."
	docker-compose run --rm agendav bash -c "cd /var/www/agendav && ./agendavcli migrations:migrate" 
