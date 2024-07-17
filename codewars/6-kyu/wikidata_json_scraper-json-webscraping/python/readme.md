## Background:
[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) is a public database with over a hundred million entries in it. You can find almost anything documented, from scientific articles to new species scientists have found.

To help developers use the site better, the website provides accessible JSON data for every submitted item. Today, you are going to program something that can read that data.

The link below leads to the page explaining how to access the corresponding JSON address of a specific Wikidata item. Although the direct URL to the data will be provided ([example](https://www.wikidata.org/wiki/Special:EntityData/Q42.json)), you might find it helpful to see the stuff your collecting from.

https://www.wikidata.org/wiki/Wikidata:Data_access

Now let's move on to the actual scraping.

## What to do:
Take a look at this labeled section of a Wikidata page:

![Photo](https://blog.reputationx.com/hs-fs/hubfs/Douglas%20Adams.jpg?width=1455&name=Douglas%20Adams.jpg)

All of this information can be found on the given JSON pages (link in the previous section). Your function should return a dictionary with the English (`en`) values of the **Identifier**, **Label**, and **Description**. The dictionary should have the keys `"ID"`, `"LABEL"`, and `"DESCRIPTION"`, respectively.

Given the URL to our example, you should return:
```
{
  "ID": "Q42",
  "LABEL": "Douglas Adams", 
  "DESCRIPTION": "English science fiction writer and humourist"
}
```

Be careful. Some information won't always be available in English, and some might not have a value associated with any language. That's because Wikidata only requires you to give one label or description. If the en label or description aren't included, put "No Label" or "No Description". Please be careful you are getting values from the "en" value, and not localized english versions such as "en-uk" or en-ca.

If you were given the URL to [this unhelpful entry](https://www.wikidata.org/wiki/Special:EntityData/Q97226458.json), you would return the following:
```
{
  "ID": "Q97226458",
  "LABEL": "No Label",
  "DESCRIPTION": "No Description"
}
```
That should be it for instructions. If you have any more questions, check out the section below, or ask them in the Discourse (after you read the section below please.)

Good Luck!

## Formal Input/Output Requirements
You are given a single argument named `url`, a string with a link to a wikidata page in JSON format. Your function should return a dictonary with keys "ID", "LABEL", and "DESCRIPTION" containing the matching "en" values.

Technical Notes
- All inputs are valid (they will all link to a scrapable JSON page)
- Since performance might be an issue, there will be 5-10 random tests (depending on language) instead of the usual 100. I don't want performance to be the focus of this kata, but if you think I should raise the number, raise a suggestion.
- This is supposed to train research skills, so not all of the information should be here. If you think there's a link I should provide, or a piece of information is missing that makes it unsolvable, head on over to the discourse.
