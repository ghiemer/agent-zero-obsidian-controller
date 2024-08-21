# ObsidianControllerTool for Agent Zero

## Overview

The `ObsidianControllerTool` is a versatile tool designed to enhance your experience with Obsidian by automating and streamlining various tasks. Whether you need to create and manage Markdown files, search and replace text, or interact with the YAML frontmatter of your notes, this tool provides the functionality you need directly within the Agent Zero framework.

## Features

- **File Management**: Create, open, and modify Markdown files within your Obsidian vault.
- **Text Manipulation**: Perform search-and-replace operations, including support for regular expressions.
- **Frontmatter Control**: Manage YAML frontmatter programmatically, adding, updating, or deleting metadata fields.
- **Efficient Navigation**: Quickly navigate to specific lines, headings, or settings within Obsidian.
- **Canvas Interaction**: Open and manage visual canvases to organize your thoughts and ideas.
- **Command Execution**: Trigger Obsidian-specific commands to automate workflows.

## Prerequisites

- **Obsidian**: Ensure that Obsidian is installed and properly configured on your system.
- **Advanced URI Plugin**: This plugin must be installed and enabled within your Obsidian vault. It facilitates the URI-based operations that the `ObsidianControllerTool` relies on.
- **Agent Zero**: This tool is designed to be used within the Agent Zero framework. You can find more about Agent Zero [here](https://github.com/frdel/agent-zero).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ghiemer/ObsidianControllerTool.git
    ```

2. **Add the Tool to Agent Zero**:
    - Place the `obsidian_controller_tool.py` script in the `tools/` directory of your Agent Zero environment.
    - Ensure that the tool is correctly referenced in the configuration files used by Agent Zero.

3. **Add Tool Description to `agent.tools.md`**:
    - Open the `agent.tools.md` file located in the Agent Zero repository.
    - Append the following lines to register the tool:

    ```markdown
    ### obsidian_controller_tool:
    Seamlessly manage and interact with your Obsidian vault using the Advanced URI Plugin. This versatile tool enables you to efficiently open, create, and edit Markdown files, ensuring your notes are always up-to-date. You can perform a variety of actions such as searching and replacing text, navigating directly to specific headings or lines, and managing metadata through frontmatter manipulation. Whether you need to append new content, execute commands within Obsidian, or organize your thoughts visually on a canvas, this tool integrates deeply with Obsidian to streamline your workflow and keep your notes structured and accessible.

    #### Available Commands:
    1. **open_file**: Opens a specific file in Obsidian.
       - **Parameters**:
         - `file_path` (str): The path to the file.
         - `line` (Optional[int]): The line number to open (optional).
         - `heading` (Optional[str]): The heading to navigate to (optional).
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to review a specific section in my notes...",
               "Let's open the file and go directly to the relevant line.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_file",
               "params": {
                   "file_path": "Projects/ProjectX/Notes.md",
                   "line": 42
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I need to check the 'Summary' section in my project notes...",
               "I'll use the tool to open the file and jump directly to that heading.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_file",
               "params": {
                   "file_path": "Projects/ProjectX/Notes.md",
                   "heading": "Summary"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I need to review the entire file without jumping to any specific section...",
               "I'll just open the file without any additional parameters.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_file",
               "params": {
                   "file_path": "Notes/DailyLog.md"
               }
           }
       }
       ```

    2. **create_or_write_file**: Creates a new file or writes to an existing file in Obsidian.
       - **Parameters**:
         - `file_path` (str): The path to the file.
         - `data` (str): The content to write to the file.
         - `mode` (str): The mode for writing ('append', 'overwrite', 'new').
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I want to add some new thoughts to my existing journal...",
               "I'll append the new content to the end of the file.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "create_or_write_file",
               "params": {
                   "file_path": "Journals/2024/April.md",
                   "data": "Today was a productive day...",
                   "mode": "append"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "The content in this note is outdated...",
               "I'll overwrite it with new, updated information.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "create_or_write_file",
               "params": {
                   "file_path": "Projects/ProjectY/Plan.md",
                   "data": "This is the updated project plan...",
                   "mode": "overwrite"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I need to start a new file for my upcoming project...",
               "I'll create the file and add some initial notes.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "create_or_write_file",
               "params": {
                   "file_path": "Projects/ProjectZ/InitialNotes.md",
                   "data": "Project Z will focus on...",
                   "mode": "new"
               }
           }
       }
       ```

    3. **execute_command**: Executes a specific command in Obsidian.
       - **Parameters**:
         - `command_id` (str): The ID of the command to execute.
         - `file_path` (Optional[str]): The path to the file (optional).
         - `line` (Optional[int]): The line number for the command (optional).
         - `mode` (Optional[str]): The mode for the command (optional).
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to update the backlinks for this note...",
               "I'll execute the command to refresh the backlinks.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "execute_command",
               "params": {
                   "command_id": "backlink-refresh",
                   "file_path": "Notes/NetworkingConcepts.md"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I want to open the command palette...",
               "I'll execute the command without targeting a specific file.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "execute_command",
               "params": {
                   "command_id": "command-palette-open"
               }
           }
       }
       ```

    4. **open_bookmark**: Opens a bookmark in Obsidian.
       - **Parameters**:
         - `bookmark` (str): The name of the bookmark.
         - `open_mode` (str): The mode to open the bookmark ('tab', 'new-pane').
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to revisit a specific bookmark in my notes...",
               "I'll open the bookmark in a new tab.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_bookmark",
               "params": {
                   "bookmark": "ImportantNotes",
                   "open_mode": "tab"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I want to compare my notes side by side...",
               "I'll open this bookmark in a new pane.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_bookmark",
               "params": {
                   "bookmark": "ProjectTimeline",
                   "open_mode": "new-pane"
               }
           }
       }
       ```

    5. **search_and_replace**: Searches and replaces text in a file in Obsidian.
       - **Parameters**:
         - `file_path` (str): The path to the file.
         - `search_term` (str): The text to search for.
         - `replace_term` (Optional[str]): The text to replace the found text with (optional).
         - `use_regex` (bool): Whether to use regular expressions for the search.
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to update a term across my notes...",
               "I'll search for the term and replace it with the updated version.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "search_and_replace",
               "params": {
                   "file_path": "Docs/Technology.md",
                   "search_term": "blockchain",
                   "replace_term": "distributed ledger technology",
                   "use_regex": false
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "I want to clean up formatting inconsistencies in my notes...",
               "I'll use a regular expression to find and replace these issues.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "search_and_replace",
               "params": {
                   "file_path": "Notes/FormattingIssues.md",
                   "search_term": "\\b[0-9]{4}\\b",
                   "replace_term": "****",
                   "use_regex": true
               }
           }
       }
       ```

    6. **manipulate_frontmatter**: Reads or writes frontmatter in an Obsidian file.
       - **Parameters**:
         - `file_path` (str): The path to the file.
         - `key` (str): The frontmatter key.
         - `value` (Optional[str]): The value to set for the key (optional).
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to add a new metadata field to this note...",
               "I'll update the frontmatter with the new key and value.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "manipulate_frontmatter",
               "params": {
                   "file_path": "Notes/Research.md",
                   "key": "status",
                   "value": "in-progress"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "The project status has changed...",
               "I'll update the status field in the frontmatter.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "manipulate_frontmatter",
               "params": {
                   "file_path": "Projects/ProjectA/Overview.md",
                   "key": "status",
                   "value": "completed"
               }
           }
       }
       ```
       ```json
       {
           "thoughts": [
               "This metadata field is no longer needed...",
               "I'll remove it from the frontmatter.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "manipulate_frontmatter",
               "params": {
                   "file_path": "Notes/OutdatedInfo.md",
                   "key": "deprecated",
                   "value": ""
               }
           }
       }
       ```

    7. **navigate_to_setting**: Navigates to a specific setting within Obsidian.
       - **Parameters**:
         - `setting_id` (str): The ID of the setting.
         - `section` (Optional[str]): The section within the setting (optional).
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to change a configuration in Obsidian...",
               "I'll navigate directly to the relevant setting.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "navigate_to_setting",
               "params": {
                   "setting_id": "editor.autoPairBrackets",
                   "section": "editor"
               }
           }
       }
       ```

    8. **open_canvas**: Opens a canvas within Obsidian.
       - **Parameters**:
         - `canvas_name` (str): The name of the canvas to open.
       - **Example usage**:
       ```json
       {
           "thoughts": [
               "I need to work on my brainstorming canvas...",
               "I'll open the relevant canvas to continue my work.",
           ],
           "tool_name": "ObsidianControllerTool",
           "tool_args": {
               "action": "open_canvas",
               "params": {
                   "canvas_name": "BrainstormingIdeas"
               }
           }
       }
       ```
    ```

## Troubleshooting

- **Tool Not Found**: Ensure that the `ObsidianControllerTool` is correctly placed in the `tools/` directory and that Agent Zero has been restarted or refreshed to recognize the new tool.
- **Advanced URI Plugin Issues**: Confirm that the Advanced URI Plugin is installed and configured properly within Obsidian.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, support, or more information, feel free to contact the development team or visit the [Agent Zero repository](https://github.com/frdel/agent-zero).
