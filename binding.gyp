{
  "targets": [
    {
      "target_name": "<(module_name)",
      "sources": [ "./setFolderReadOnly.cc" ]
    },
	{
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [  ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
