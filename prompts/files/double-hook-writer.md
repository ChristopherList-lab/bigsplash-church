# Double Hook Writer

**Purpose:** Claude writes two-part hooks for your Reels, so people stop in the first second and stay for the rest.

From Big Splash (bigsplash.church). Free to use and share. Change it to fit your church.

## Set it up

1. Add this file to a Claude project. Add church-social-voice.md too if you have it.
2. In a chat, give Claude the Reel's topic and the cards that come after the hook.
3. Ask for 10 double hooks, then pick one yourself.

A person picks the final hook and checks that the Reel pays it off.

## The two hooks

- **Hook 1** is on screen from the first frame. At most 6 words. It's a bold claim or a question a church leader can't scroll past.
- **Hook 2** rises in about 1.5 seconds later, under hook 1. At most 8 words. It opens a question or raises the stakes, so people keep watching.
- The cards after that pay it off. If the Reel can't answer hook 2, cut the hook.

Instagram's own Reels guide says strong text on the first frame can work as well as a great thumbnail. So hook 1 goes on frame one, and it doubles as your cover.

Source: Instagram, "How to make Instagram Reels: the complete 2026 guide" (about.instagram.com/blog/tips-and-tricks/how-to-make-instagram-reels)

---

## Instructions for Claude

Write double hooks for church Reels. The viewer is a pastor or church staff member scrolling Instagram on a phone.

### Rules

- Hook 1: 6 words or fewer and 32 characters or fewer, so it fits in big type.
- Hook 2: 8 words or fewer and 50 characters or fewer.
- Use plain 5th-grade words. Contractions and natural questions are fine.
- Make hook 2 add something new. Don't repeat hook 1 in other words.
- Pick one short word in hook 1 to highlight and wrap it like this: [[first]]. Keep it to one word of 9 letters or fewer.
- Every hook must be true, and the Reel must pay it off. Name the card that does.
- No riddle hooks ("You won't believe this one"), no fake urgency, no shock for its own sake.
- No numbers unless I gave you the number and its source.
- No em dashes and no hype adverbs.

### Angles that stop church leaders

- A line that says what pastors feel and don't say out loud.
- A surprising finding I gave you, with its source.
- A short quote from a pastor or leader, word for word, with their name.
- A common church mistake with an easy fix.
- A free tool or prompt they can copy, if the Reel gives it away.

### Output

Give me a table with these columns:

| # | Hook 1 | Hook 2 | Card that pays it off | Why a pastor stops |
|---|---|---|---|---|

Then star your best two and give the reason for each in one line. Flag any hook that needs a source.

---

## Prompt to copy

> Write 10 double hooks for a Reel about [topic]. Hook 1: 6 words max, on screen in the first second. Hook 2: 8 words max, shows 1.5 seconds later and raises a question the Reel answers. Plain 5th-grade words. No clickbait. Here are the cards that follow: [paste].

## Examples

Both of these ran on our own Reels.

**Topic:** testing church posts with Claude before they go out

- Hook 1: Your post gets one [[glance]]
- Hook 2: We test ours on a busy pastor first.
- Paid off by: the card with the test prompt.

**Topic:** a staff AI policy

- Hook 1: Some jobs stay [[human]]
- Hook 2: Does your staff know which ones?
- Paid off by: the cards on what AI drafts and what stays with people.

**A hook we'd cut**

- Hook 1: This changed everything for us
- Hook 2: Wait for number 4.
- A pastor can't tell the topic from this, and "everything" promises more than a 19-second Reel can show.
