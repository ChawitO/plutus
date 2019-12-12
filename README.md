# Plutus
## Overview
This project was assigned to me by General Assembly during Software Engineering Immersive course. This was done in 3 people group with [Vikram](https://github.com/vikram1510) and [Bhuwan](https://github.com/bhuone-garbu), with the aim to build a complete website with the frontend along with our own backend API and database.

We chose to build a bill splitting app, inspired by Splitwise, which records and shows bill splitting between friends. It is designed to be mobile first, so if viewing on desktop please try to narrow the width to about 380px.

The project is currently deployed at https://plutus-cbv.herokuapp.com/.

<img src="https://i.imgur.com/qcd8EoC.png" title="source: imgur.com" height="400"/>

## Timeframe and Team
1 week and 3 people

## Technologies
* React
* SCSS
* Node.js
* Python
* Django
* PostgreSQL
* Webpack
* Pusher's Channel - Managed websocket connections and allows for real-time notifications

# Instructions
<img src="https://i.imgur.com/m4CDdjs.png" title="source: imgur.com" height="400"/>

After you sign up and then sign in, you can start creating your expense and split your bills with friends.

<img src="https://i.imgur.com/g1t4kGc.png" title="source: imgur.com" height="400"/>

The image above shows the create expense form. You can specify who paid the bill, and what type of split do you want. For splits, there are unequal, equal, and percentage based splitting.

<img src="https://i.imgur.com/biPpa1I.png" title="source: imgur.com" height="400"/>

The image above shows the home page after you signed in, assuming you had made some expenses before. This page shows your total balance between your friends a the top. And below it shows if you owe your friends or they owe you. Clicking on your friend will lead to a detailed page showing all the bills between you and your friend.

<img src="https://i.imgur.com/iZzp55J.png" title="source: imgur.com" height="400"/>

The image above shows the detailed bill listings between you and your friends. The greyed out listing represents expense that was deleted, it is not included in calculating the total owed amount, but can be recovered at any time. You can also click on the expense itself to see all friends involved in that specific expense.

<img src="https://i.imgur.com/4S9bFWd.png" title="source: imgur.com" height="400"/>

The image above shows an expense show page. With an equal splitting between 3 people, where Rakesh paid £18 in total, but owes £6 to the group, and the other 2 each owes £6 to the group.

You can also add comments to the expense

<img src="https://i.imgur.com/pJyga8I.png" title="source: imgur.com" height="400"/>

There is also a real-time notification system. If someone add or settle an expense, you will be notified in this page.

# Process
On this last project at General Assembly's Software Engineering Immersive, we had the chance to choose our own teammate. So us 3 teamed up and decided to work hard on this last one.

We wanted to build a project that has real world usage, while we wanted to do something original, we went with Splitwise as the inspiration. We used it frequently and so were familiar with it, we were curious on how it works and so it was an obvious choice for us.

We all had a hand in all parts, frontend, backend, and styling. However my major contributions were mainly the frontend and styling.

I set the main styling guideline for our project, with reusable SCSS components which my coworkers could easily use. I tried to make it looks professional and clean.

While my teammates worked on the backend code for user model, I handled the frontend user register and signin form, along with the related API calls to our backend.

I handled the expense forms and interaction with our backend, sending data, displaying information on index and show page, and navigation bar. The code I wrote for the expense index listing is also reused in the notification page and when showing expenses between the current user and a friend.
```js
// The expense form
<form onSubmit={this.onSubmit}>
  <div>
    <input id='description' placeholder=' ' onChange={this.onChange} />
    <label htmlFor='description'>Description</label>
    {errors.description && <div className='error-message'>{errors.description}</div>}
  </div>
  <div>
    <input id='amount' type='number' placeholder=' ' onChange={this.onChange} />
    <label htmlFor='amount'>Amount</label>
    {errors.amount && <div className='error-message'>{errors.amount}</div>}
  </div>
  <div className='select-wrapper'>
    <p>Payer</p>
    <select id='payer' value={data.payer.id} onChange={this.onChange}>
      {friends && friends.map(({ id, username }) => (
        <option key={id} value={id}>{username}</option>
      ))}
    </select>
  </div>
  <div className='select-wrapper'>
    <p>Splits</p>
    <select id='split_type' value={data.split_type} onChange={this.onChange}>
      <option value='equal'>Equal</option>
      <option value='unequal'>Unequal</option>
      <option value='percentage'>Percentage</option>
    </select>
  </div>
  <div>
    {friends && friends.map(({ id, username }) => (
      <div key={id} className='debtor-wrapper'>
        <label htmlFor={id} className='debtor'>{username}</label>
        <div>
          <div>{data.split_type === 'unequal' ? '£' : data.split_type === 'percentage' ? '%' : null}</div>
          <input id={id} type={data.split_type === 'equal' ? 'checkbox' : 'number'} placeholder='0' onChange={this.onSplitChange} />
        </div>
      </div>
    ))}
  </div>
  <button type='submit'>Create</button>
</form>
```

For the backend, I did the comments model and its serializers, along with its frontend.
```py3
# Comment is the child of the Expense
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    text = models.CharField(max_length=200) # the actual user comment text
    # CASCADE - When the referenced object is deleted, also delete the objects that have references to it
    expense = models.ForeignKey(Expense, related_name='comments', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.creator}: {self.text}'
```



# Challenges
* When we encounted a problem, we were not sure if it was a frontend or a backend problem. This was especially true of our expense model, which is quite complicated. When we encounted a problem, we was unsure if we should fix it at the frontend or the backend. In the end we decided that it would be better to refactor and improve the backend, so that it is easier to understand and use.
* Designing for mobile while working on desktop has some complications. The hover effects on desktop don't work properly on mobile.
* Designing SCSS to be reuseable is complicated given then short time we had.

# Wins
* We worked together really well as a team. The feeling of being a part of a project that resulted in something better than what I could have done alone is very satisfying.
* I get to create a project that works well and has real world implication.
* Learnt much more about React
* Learnt how to design reusable SCSS codes that other teammates can easily understand and use
* Learnt about Django and how language other than JavaScript handle backend

# Further Features
* I would like to learn React Native and make a proper mobile app for this
* Implement PayPal
* Implement OAuth from Facebook and Google
* There are some bugs which we couldn't find the reasons, would be nice to fix them.
