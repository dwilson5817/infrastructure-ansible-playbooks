# Ansible Playbooks

![Pipeline status badge](https://gitlab.dylanw.dev/infrastructure/ansible-playbooks/badges/main/pipeline.svg)

A collection of Ansible configuration to manage VMs on my dedicated server.

### Development

To work with these playbooks locally, follow these steps:

1. **Setup a Python virtual environment:**
   ```bash
   python3 -m venv .venv
   source venv/bin/activate
   ```

2. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ansible Galaxy requirements:**
   ```bash
   ansible-galaxy install -r requirements.yml
   ```

4. **Configure environment variables:**
   Set the following variables to authenticate with HashiCorp Vault:
   ```bash
   export VAULT_ADDR='your-vault-address'
   export VAULT_TOKEN='your-vault-token'
   ```

5. **Run the Ansible playbooks:**
   ```bash
   ansible-playbook -i london.proxmox.yml playbooks/main.yml
   ```

### Deployment

The following machine types are managed within this repository. All nodes are initialized with a baseline configuration including system package management, user account provisioning, and SSH authorized key distribution.

- **Proxmox**: Provisions Proxmox Virtual Environment (PVE) nodes and virtual machines using `cloud-init`.
- **Desktop**: Configures Linux workstations with development toolchains, including HashiCorp Vault, Docker, and Python build dependencies.
- **Game**: Installs the Docker runtime and Pterodactyl Wings for containerized game server orchestration.
- **Mail**: Deploys the Mailcow Dockerized suite and synchronizes DNS records for managed zones.
- **Git**: Installs and configures self-hosted GitLab instances.
- **Runner**: Provisions and registers GitLab Runner instances for CI/CD execution.
- **Monitor**: Deploys Prometheus for metric collection and Grafana for data visualization.
- **Social**: Provisions BlueSky Personal Data Servers (PDS).
- **SQL**: Manages MariaDB instances supporting game servers and web applications.
- **Web**: Deploys PHP applications, including directory structures and environment-specific configurations.

### License

Licensed under the GNU General Public License v3.0.

```
Ansible Playbooks - Ansible configuration for managing Proxmox
Copyright (C) 2020 Dylan Wilson

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

Full license available [here](https://gitlab.dylanw.dev/infrastructure/ansible-playbooks/-/raw/main/LICENSE).
