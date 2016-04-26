#!/bin/bash
set -e

export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_DB

exec "$@"
