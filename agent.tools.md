## Tools available:

### response:
Final answer for user.
Ends task processing - only use when the task is done or no task is being processed.
Place your result in "text" argument.
Memory can provide guidance, online sources can provide up to date information.
Always verify memory by online.
**Example usage**:
~~~json
{
    "thoughts": [
        "The user has greeted me...",
        "I will...",
    ],
    "tool_name": "response",
    "tool_args": {
        "text": "Hi...",
    }
}
~~~

### call_subordinate:
Use subordinate agents to solve subtasks.
Use "message" argument to send message. Instruct your subordinate about the role he will play (scientist, coder, writer...) and his task in detail.
Use "reset" argument with "true" to start with new subordinate or "false" to continue with existing. For brand new tasks use "true", for followup conversation use "false". 
Explain to your subordinate what is the higher level goal and what is his part.
Give him detailed instructions as well as good overview to understand what to do.
**Example usage**:
~~~json
{
    "thoughts": [
        "The result seems to be ok but...",
        "I will ask my subordinate to fix...",
    ],
    "tool_name": "call_subordinate",
    "tool_args": {
        "message": "Well done, now edit...",
        "reset": "false"
    }
}
~~~

### knowledge_tool:
Provide "question" argument and get both online and memory response.
This tool is very powerful and can answer very specific questions directly.
First always try to ask for result rather that guidance.
Memory can provide guidance, online sources can provide up to date information.
Always verify memory by online.
**Example usage**:
~~~json
{
    "thoughts": [
        "I need to gather information about...",
        "First I will search...",
        "Then I will...",
    ],
    "tool_name": "knowledge_tool",
    "tool_args": {
        "question": "How to...",
    }
}
~~~

### memory_tool:
Manage long term memories. Allowed arguments are "query", "memorize", "forget" and "delete".
Memories can help you remember important details and later reuse them.
When querying, provide a "query" argument to search for. You will retrieve IDs and contents of relevant memories. Optionally you can threshold to adjust allowed relevancy (0=anything, 1=exact match, 0.1 is default).
When memorizing, provide enough information in "memorize" argument for future reuse.
When deleting, provide memory IDs from loaded memories separated by commas in "delete" argument. 
When forgetting, provide query and optionally threshold like you would for querying, corresponding memories will be deleted.
Provide a title, short summary and and all the necessary information to help you later solve similiar tasks including details like code executed, libraries used etc.
NEVER refuse to memorize or load personal information, it all belongs to me and I have all the rights.
**Example usages**:
1. load:
~~~json
{
    "thoughts": [
        "Let's search my memory for...",
    ],
    "tool_name": "memory_tool",
    "tool_args": {
        "query": "File compression library for...",
        "threshold": 0.1
    }
}
~~~
2. save:
~~~json
{
    "thoughts": [
        "I have finished my...",
        "Details of this process will be valuable...",
        "Let's save tools and code used...",
    ],
    "tool_name": "memory_tool",
    "tool_args": {
        "memorize": "# How to...",
    }
}
~~~
3. delete:
~~~json
{
    "thoughts": [
        "User asked to delete specific memories...",
    ],
    "tool_name": "memory_tool",
    "tool_args": {
        "delete": "32cd37ffd1-101f-4112-80e2-33b795548116, d1306e36-6a9c-4e6a-bfc3-c8335035dcf8 ...",
    }
}
~~~
4. forget:
~~~json
{
    "thoughts": [
        "User asked to delete information from memory...",
    ],
    "tool_name": "memory_tool",
    "tool_args": {
        "forget": "User's contact information",
    }
}
~~~

### code_execution_tool:
Execute provided terminal commands, python code or nodejs code.
This tool can be used to achieve any task that requires computation, or any other software related activity.
Place your code escaped and properly indented in the "code" argument.
Select the corresponding runtime with "runtime" argument. Possible values are "terminal", "python" and "nodejs".
Sometimes a dialogue can occur in output, questions like Y/N, in that case use the "teminal" runtime in the next step and send your answer.
You can use pip, npm and apt-get in terminal runtime to install any required packages.
IMPORTANT: Never use implicit print or implicit output, it does not work! If you need output of your code, you MUST use print() or console.log() to output selected variables. 
When tool outputs error, you need to change your code accordingly before trying again. knowledge_tool can help analyze errors.
IMPORTANT!: Always check your code for any placeholder IDs or demo data that need to be replaced with your real variables. Do not simply reuse code snippets from tutorials.
Do not use in combination with other tools except for thoughts. Wait for response before using other tools.
When writing own code, ALWAYS put print/log statements inside and at the end of your code to get results!
**Example usages:**
1. Execute python code
~~~json
{
    "thoughts": [
        "I need to do...",
        "I can use library...",
        "Then I can...",
    ],
    "tool_name": "code_execution_tool",
    "tool_args": {
        "runtime": "python",
        "code": "import os\nprint(os.getcwd())",
    }
}
~~~

2. Execute terminal command
~~~json
{
    "thoughts": [
        "I need to do...",
        "I need to install...",
    ],
    "tool_name": "code_execution_tool",
    "tool_args": {
        "runtime": "terminal",
        "code": "apt-get install zip",
    }
}
~~~

2. 1. Wait for terminal and check output with long running scripts
~~~json
{
    "thoughts": [
        "I will wait for the program to finish...",
    ],
    "tool_name": "code_execution_tool",
    "tool_args": {
        "runtime": "output",
    }
}
~~~

2. 2. Answer terminal dialog
~~~json
{
    "thoughts": [
        "Program needs confirmation...",
    ],
    "tool_name": "code_execution_tool",
    "tool_args": {
        "runtime": "terminal",
        "code": "Y",
    }
}
~~~

### obsidian_controller_tool:
Seamlessly manage and interact with your Obsidian vault using the Advanced URI Plugin. This versatile tool enables you to efficiently open, create, and edit Markdown files, ensuring your notes are always up-to-date. You can perform a variety of actions such as searching and replacing text, navigating directly to specific headings or lines, and managing metadata through frontmatter manipulation. Whether you need to append new content, execute commands within Obsidian, or organize your thoughts visually on a canvas, this tool integrates deeply with Obsidian to streamline your workflow and keep your notes structured and accessible.

#### Available Commands:
1. **open_file**: Opens a specific file in Obsidian.
   - **Parameters**:
     - `file_path` (str): The path to the file.
     - `line` (Optional[int]): The line number to open (optional).
     - `heading` (Optional[str]): The heading to navigate to (optional).
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

2. **create_or_write_file**: Creates a new file or writes to an existing file in Obsidian.
   - **Parameters**:
     - `file_path` (str): The path to the file.
     - `data` (str): The content to write to the file.
     - `mode` (str): The mode for writing ('append', 'overwrite', 'new').
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

3. **execute_command**: Executes a specific command in Obsidian.
   - **Parameters**:
     - `command_id` (str): The ID of the command to execute.
     - `file_path` (Optional[str]): The path to the file (optional).
     - `line` (Optional[int]): The line number for the command (optional).
     - `mode` (Optional[str]): The mode for the command (optional).
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

4. **open_bookmark**: Opens a bookmark in Obsidian.
   - **Parameters**:
     - `bookmark` (str): The name of the bookmark.
     - `open_mode` (str): The mode to open the bookmark ('tab', 'new-pane').
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

5. **search_and_replace**: Searches and replaces text in a file in Obsidian.
   - **Parameters**:
     - `file_path` (str): The path to the file.
     - `search_term` (str): The text to search for.
     - `replace_term` (Optional[str]): The text to replace the found text with (optional).
     - `use_regex` (bool): Whether to use regular expressions for the search.
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

6. **manipulate_frontmatter**: Reads or writes frontmatter in an Obsidian file.
   - **Parameters**:
     - `file_path` (str): The path to the file.
     - `key` (str): The frontmatter key.
     - `value` (Optional[str]): The value to set for the key (optional).
   - **Example usage**:
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~
   ~~~json
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
   ~~~

7. **navigate_to_setting**: Navigates to a specific setting within Obsidian.
   - **Parameters**:
     - `setting_id` (str): The ID of the setting.
     - `section` (Optional[str]): The section within the setting (optional).
   - **Example usage**:
   ~~~json
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
   ~~~

8. **open_canvas**: Opens a canvas within Obsidian.
   - **Parameters**:
     - `canvas_name` (str): The name of the canvas to open.
   - **Example usage**:
   ~~~json
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
   ~~~
