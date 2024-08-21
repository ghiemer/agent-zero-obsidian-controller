# python/tools/obsidian_controller_tool.py

import webbrowser
import os
import re
from typing import Any, Dict, Optional

class ObsidianControllerTool:
    """
    Tool for interacting with Obsidian using the Advanced URI Plugin.
    """

    def __init__(self, vault_name: str):
        self.vault_name = vault_name

    def execute(self, action: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a specified action with parameters.

        :param action: The action to perform (e.g., 'open_file', 'create_or_write_file').
        :param params: The parameters for the action.
        :return: Result of the action execution.
        """
        if not params:
            params = {}

        method = getattr(self, action, None)
        if callable(method):
            return method(**params)
        else:
            raise ValueError(f"Action '{action}' is not recognized or not callable.")

    def _construct_uri(self, params: Dict[str, Any]) -> str:
        """
        Helper method to construct an Obsidian URI.
        """
        base_uri = f"obsidian://advanced-uri?vault={self.vault_name}"
        for key, value in params.items():
            if value is not None:
                base_uri += f"&{key}={value}"
        return base_uri

    def _execute_uri(self, uri: str):
        """
        Execute the constructed URI to interact with Obsidian.
        """
        webbrowser.open(uri)

    def open_file(self, file_path: str, line: Optional[int] = None, heading: Optional[str] = None) -> Dict[str, Any]:
        """
        Open a file in Obsidian.

        :param file_path: Path to the file.
        :param line: Line number to open (optional).
        :param heading: Heading to navigate to (optional).
        :return: Confirmation of action.
        """
        params = {"filepath": file_path, "line": line, "heading": heading}
        uri = self._construct_uri(params)
        self._execute_uri(uri)
        return {"status": "file opened", "file_path": file_path, "line": line, "heading": heading}

    def create_or_write_file(self, file_path: str, data: str, mode: str = 'append') -> Dict[str, Any]:
        """
        Create or write to a file in Obsidian.

        :param file_path: Path to the file.
        :param data: Data to write.
        :param mode: Mode ('append', 'overwrite', 'new').
        :return: Confirmation of action.
        """
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        if mode == 'append' and os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write("\n" + data)
        elif mode == 'overwrite' or mode == 'new':
            with open(file_path, 'w') as file:
                file.write(data)
        else:
            raise ValueError(f"Unsupported mode: {mode}")
        
        return {"status": "file written", "file_path": file_path, "mode": mode}

    def execute_command(self, command_id: str, file_path: Optional[str] = None, line: Optional[int] = None, mode: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute a command in Obsidian.

        :param command_id: ID of the command to execute.
        :param file_path: Path to the file (optional).
        :param line: Line number (optional).
        :param mode: Mode for the command (optional).
        :return: Confirmation of action.
        """
        params = {"commandid": command_id, "filepath": file_path, "line": line, "mode": mode}
        uri = self._construct_uri(params)
        self._execute_uri(uri)
        return {"status": "command executed", "command_id": command_id}

    def open_bookmark(self, bookmark: str, open_mode: str = 'tab') -> Dict[str, Any]:
        """
        Open a bookmark in Obsidian.

        :param bookmark: Name of the bookmark.
        :param open_mode: Mode to open the bookmark ('tab', 'new-pane').
        :return: Confirmation of action.
        """
        params = {"bookmark": bookmark, "openmode": open_mode}
        uri = self._construct_uri(params)
        self._execute_uri(uri)
        return {"status": "bookmark opened", "bookmark": bookmark}

def search_and_replace(self, file_path: str, search_term: str, replace_term: Optional[str] = None, use_regex: bool = False) -> Dict[str, Any]:
    """
    Search and replace text in a file.

    :param file_path: Path to the file.
    :param search_term: Term to search for.
    :param replace_term: Term to replace with (optional).
    :param use_regex: Whether to use regex for the search.
    :return: Confirmation of action.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r') as file:
        content = file.read()

    if use_regex:
        # Use re.sub with replace_term defaulting to an empty string if it's None
        content = re.sub(search_term, replace_term or "", content)
    else:
        # Simple replace without regex
        content = content.replace(search_term, replace_term or "")

    with open(file_path, 'w') as file:
        file.write(content)

    return {"status": "search and replace done", "file_path": file_path}

    def manipulate_frontmatter(self, file_path: str, key: str, value: Optional[str] = None) -> Dict[str, Any]:
        """
        Manipulate the frontmatter of a file.

        :param file_path: Path to the file.
        :param key: Frontmatter key.
        :param value: Value to set (optional).
        :return: Confirmation of action.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        frontmatter_started = False
        frontmatter_ended = False
        new_lines = []
        for line in lines:
            if line.strip() == "---":
                if frontmatter_started:
                    frontmatter_ended = True
                frontmatter_started = True
            if frontmatter_started and not frontmatter_ended:
                if line.startswith(key + ":"):
                    if value:
                        new_lines.append(f"{key}: {value}\n")
                    continue
            new_lines.append(line)

        if not frontmatter_started:
            new_lines.insert(0, "---\n")
            new_lines.insert(1, f"{key}: {value}\n")
            new_lines.insert(2, "---\n")

        with open(file_path, 'w') as file:
            file.writelines(new_lines)

        return {"status": "frontmatter manipulated", "file_path": file_path, "key": key}

    def navigate_to_setting(self, setting_id: str, section: Optional[str] = None) -> Dict[str, Any]:
        """
        Navigate to a specific setting in Obsidian.

        :param setting_id: ID of the setting.
        :param section: Section of the setting (optional).
        :return: Confirmation of action.
        """
        params = {"settingid": setting_id, "settingsection": section}
        uri = self._construct_uri(params)
        self._execute_uri(uri)
        return {"status": "navigated to setting", "setting_id": setting_id}

    def open_canvas(self, canvas_name: str) -> Dict[str, Any]:
        """
        Open a canvas in Obsidian.

        :param canvas_name: Name of the canvas.
        :return: Confirmation of action.
        """
        params = {"filepath": f"{canvas_name}.canvas"}
        uri = self._construct_uri(params)
        self._execute_uri(uri)
        return {"status": "canvas opened", "canvas_name": canvas_name}
