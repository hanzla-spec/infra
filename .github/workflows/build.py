name: Manual Dispatch Workflow

on:
  workflow_dispatch:
    inputs:
      commit_id:
        description: 'Commit ID'
        required: true

jobs:
  print_commit_id:
    runs-on: ubuntu-latest
    name: Commit ID for SHA ${{ github.event.inputs.commit_id }}
    steps:
      - name: Print Workflow Name and Commit ID
        run: |
          echo "Running Manual Dispatch Workflow for Commit ID: ${{ github.event.inputs.commit_id }}"
