---
name: deepseek-chat
description: "Use when: you need to send a chat message to DeepSeek from the browser and manage a DeepSeek conversation session."
---

# DeepSeek Chat Skill

This skill captures the workflow for interacting with DeepSeek through the browser and automating the chat send process when possible.

## Workflow

1. Confirm the target chat environment
   - Verify the browser is on `https://chat.deepseek.com/` or an active DeepSeek chat session.
   - Ensure the user is logged in and the input box is visible.

2. Prepare the message
   - Ask the user for the chat message text.
   - If no message is provided, offer to send a simple greeting or prompt.

3. Send the message
   - Locate the DeepSeek chat input box.
   - Populate the message text.
   - Trigger the send action by pressing Enter or clicking the send button.

4. Confirm delivery
   - Verify the new message appears in the chat history.
   - If the send action fails, use page debugging tools to identify a working send control.

5. Document results
   - Save the skill and the relevant page structure to the AIWork repository for future reuse.

## Quality checks

- The chat page is authenticated.
- The message is entered into the correct DeepSeek input box.
- The message is actually sent and appears in the conversation.
- The skill instructions and optional tool code are stored in AIWork.
