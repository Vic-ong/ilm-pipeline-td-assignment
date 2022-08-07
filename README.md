# ILM Pipeline TD assignment

## Assignment

Implement a simple priority queue. Assume an incoming stream of dictionaries containing two keys; command to be executed and priority. Priority is an integer value [0, 10], where work items of the same priority are processed in the order they are received.

## Approach

xxx

## Development setup

xxx

## Questions

**Please explain Big-O notation in simple terms.**

Big-O notation is a way to describe how well an algorithm performs as its input grows.

**What are the most important things to look for when reviewing another team member's code?**

The most important things I look for when reviewing another team member's code are complexity, functionality, and consistency.

*Complexity*
- Is code implementation more complicated than it should be? The code should be written in a clean and organized manner without sacrificing performance
- If the code needs to be more complex, ensure that there are well-written comments. Complex code can introduce bugs if a developer who's new to this section, comes in and make changes.

*Functionality*
- The code should do what the developer intends it to do (or rather what the feature ticket states)
- Does the code implementation handle edge cases and evaluate if this is the right place to handle certain edge cases throughout the chain of execution

*Consistency*
- The code should follow coding standards defined by the team (e.g. naming conventions and folder structure)

**Describe a recent interaction with someone who was non-technical. What did you need to communicate and how did you do it?**

I recently worked on an animated film project that is real-time rendered in Unreal Engine. Our team consists of one developer (me), one 3D artist, one 2D artist, and two writers. The main character is motion captured at a MOCAP studio but we realized that the model we used to record the MOCAP cannot be imported into Unreal Engine.

Given that the 3D artist created the model and rigged it in MAYA whereas I have the expertise in Unreal Engine, we had an initial discussion to figure out what Unreal Engine requires of the model and how the artist rig the model in MAYA. It seems like the bone structure needs to be grouped in a certain way and a couple of groups need to be renamed. Seems fairly straightforward, but we have over 50 FBX animation files to fix with a tight deadline.

Next, I try to do a manual fix in MAYA and test the import in Unreal while verifying with the artist if this fix would affect the animations. With one successful fix, I wrote a script that would go through each file to search for the skeleton root group and traverse down the tree to rename a couple of joints and move the grouping. What would've taken 2 days for the artist or me to manually fix each file has been cut down to just 3 hours.

All I have to do next is to commit the updated files to the source control (we use Git) and the artist could just pull and use the fixed animations in Unreal Engine.
