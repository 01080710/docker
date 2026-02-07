#!/bin/bash

# Generate random SUPERSET_SECRET_KEY with only letters and numbers
SECRET_KEY=$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 32)

# Write it into docker/.env (overwrite if exists)
if grep -q "^SUPERSET_SECRET_KEY=" docker/.env; then
  sed -i.bak "s|^SUPERSET_SECRET_KEY=.*|SUPERSET_SECRET_KEY=${SECRET_KEY}|" docker/.env
else
  echo "SUPERSET_SECRET_KEY=${SECRET_KEY}" >> docker/.env
fi

echo "Generated SUPERSET_SECRET_KEY in docker/.env"
