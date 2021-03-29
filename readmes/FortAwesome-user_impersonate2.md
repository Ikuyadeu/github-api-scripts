## `user_impersonate2`

[![Install gem](https://badge.fury.io/rb/user_impersonate2.png)](https://rubygems.org/gems/user_impersonate2)
[![Build status](https://travis-ci.org/rcook/user_impersonate2.png)](https://travis-ci.org/rcook/user_impersonate2)
[![Coverage status](https://coveralls.io/repos/rcook/user_impersonate2/badge.png?branch=master)](https://coveralls.io/r/rcook/user_impersonate2)

## Note

This is a fork of Engine Yard's no-longer-maintained [`user_impersonate`](https://github.com/engineyard/user_impersonate)
gem and is its official successor. It supports Rails 3.2.x and Rails 4 and has
been tested against Ruby 1.9.3, 2.0.0 and 2.1.0, 2.2, 2.3.1.

## Overview

`user_impersonate2` allows staff users to impersonate normal users: to see what
they see and to only do what they can do.

This concept and code was extracted from [Engine Yard Cloud](http://www.engineyard.com/products/cloud),
which Engine Yard uses to support customer remotely.

This Rails engine currently supports the following Rails authentication systems:

* [Devise](https://github.com/plataformatec/devise)

## Links

* [Wiki](https://github.com/rcook/user_impersonate2/wiki) (includes tutorials
etc.)

## Example usage

When you are impersonating a user you see what they see with a header section
above. By default, this will be red.

## Installation

Add the gem to your Rails application's `Gemfile` and run `bundle`:

```ruby
gem 'user_impersonate2', :require => 'user_impersonate'
```

Note that `:require => 'user_impersonate'` is required as this gem currently
maintains the same internal directory structure as the original
[`user_impersonate`](https://github.com/engineyard/user_impersonate) gem. This
may change in future versions but is retained for compatibility for the time
being.

Run the (sort of optional) generator:

```bash
bundle
rails generate user_impersonate
```

This adds the following line to your `config/routes.rb` file:

```ruby
mount UserImpersonate::Engine => "/impersonate", as: "impersonate_engine"
```

It also generates a default initializer under `config/initializers/user_impersonate2.rb`.

Make sure that your layout files include the standard flashes since these are
used to communicate information and error messages to the user:

```erb
<p class="notice"><%= flash[:notice] %></p>
<p class="alert"><%= flash[:error] %></p>
```

Next, add the impersonation header to your layouts:

```erb
<% if current_staff_user %>
  <%= render 'user_impersonate/header' %>
<% end %>
```

Next, add the "staff" concept to your `User` model.

To test the engine out, make all users staff!

```ruby
# app/models/user.rb

def staff?
  true
end

# String to represent a user (e-mail, name, etc.)
def to_s
  email
end
```

You can now go to [http://localhost:3000/impersonate](http://localhost:3000/impersonate)
to see the list of users, except your own user account. Click on the
"Impersonate" link to impersonate that user and to see the magic!

## Integration

To support this Rails engine, you need to add some things.

* `current_user` helper within controllers and helpers
* `current_user.staff?` - your `User` model needs a `staff?` method to identify
if the current user is allowed to impersonate other users; if this method is
missing, no user can access impersonation system

### `User#staff?`

One way to add the `staff?` helper is to add a column to your `User` model:

```bash
rails generate migration add_staff_to_users staff:boolean
rake db:migrate db:test:prepare
```

## Customization

### Header

You can override the bright red header by creating a `app/views/user_impersonate/_header.html.erb`
file (or whatever template system you like).

The `app/views/user_impersonate/_header.html.haml` HAML partial for this header
would be:

```haml
%div#impersonating
  .impersonate-controls.page
    .impersonate-info.grid_12
      You (
      %span.admin_name= current_staff_user
      ) are impersonating
      %span.user_name= link_to current_user, url_for([:admin, current_user])
      ( User id:
      %span.user_id= current_user.id
      )
      - if current_user.no_accounts?
        ( No accounts )
      - else
        ( Account name:
        %span.account_id= link_to current_user.accounts.first, url_for([:admin, current_user.accounts.first])
        , id:
        %strong= current_user.accounts.first.id
        )
    .impersonate-buttons.grid_12
      = form_tag url_for([:ssh_key, :admin, current_user]), :method => "put" do
        %span Support SSH Key
        = select_tag 'public_key', options_for_select(current_staff_user.keys.map {|k| k})
        %button{:type => "submit"} Install SSH Key
      or
      = form_tag [:admin, :revert], :method => :delete, :class => 'revert-form' do
        %button{:type => "submit"} Revert to admin
```

### Redirects

By default, when you impersonate and when you stop impersonating a user you are
redirected to the root URL.

Alternative paths can be configured in the initializer `config/initializers/user_impersonate.rb`
created by the `user_impersonate` generator described above.

```ruby
# config/initializers/user_impersonate.rb
module UserImpersonate
  class Engine < Rails::Engine
    config.redirect_on_impersonate = '/'
    config.redirect_on_revert = '/impersonate'
  end
end
```

### User model and lookup

By default, `user_impersonate2` assumes the user model is named `User`, that you
use `User.find(id)` to find a user given its ID, use `some_user.id` to get the
related ID value and that your user model has a `staff?` attribute that returns
`true` if the corresponding user is staff and `false` otherwise.

You can change this default behaviour in the initializer `config/initializers/user_impersonate.rb`.

```ruby
# config/initializers/user_impersonate.rb
module UserImpersonate
  class Engine < Rails::Engine
    config.user_class = 'User'
    config.user_finder = 'find'
    config.user_id_column = 'id'
    config.user_is_staff_method = 'staff?'
  end
end
```

By default, `user_impersonate2` will use the same model for staff/admin users
as that described above for regular users. Some configurations, using
frameworks such as [Active Admin](http://activeadmin.info/), for example, use a
different model for staff/admin users. `user_impersonate2`'s default behaviour
can be overridden using the following initializer settings:

```ruby
# config/initializers/user_impersonate.rb
module UserImpersonate
  class Engine < Rails::Engine
    # For Active Admin "AdminUser" model, use 'authenticate_admin_user!'
    config.authenticate_user_method = 'authenticate_admin_user!'

    # For Active Admin "AdminUser" model, use 'AdminUser'
    config.staff_class = 'AdminUser'

    # Staff user model lookup method
    config.staff_finder = 'find'

    # For Active Admin "AdminUser" model, use 'current_admin_user'
    config.current_staff = 'current_admin_user'
  end
end
```

### Spree-specific stuff

Modify `User` and add a `current_user` helper:

```ruby
Spree::User.class_eval do
  def staff?
    has_spree_role?('admin')
  end

  def to_s
    email
  end
end

ApplicationController.class_eval do
  helper_method :current_user
  def current_user
    spree_current_user
  end
end
```

Use the following initializer:

```ruby
# config/initializers/user_impersonate.rb
module UserImpersonate
  class Engine < Rails::Engine
    config.user_class = 'Spree::User'
    config.user_finder = 'find'
    config.user_id_column = 'id'
    config.user_is_staff_method = 'staff?'
    config.authenticate_user_method = 'authenticate_spree_user!'
    config.redirect_on_impersonate = '/'
    config.redirect_on_revert = '/'
    config.user_name_column = 'users'
  end
end
```

Use deface to add the header:

```ruby
Deface::Override.new(:virtual_path => "spree/layouts/spree_application",
                     :name => "impersonate_header", 
                     :insert_before => "div.container",
                     :text => "<% if current_staff_user %><%= render 'user_impersonate/header' %><% end %>")
```

## Contributing

See [`.travis.yml`](https://github.com/rcook/user_impersonate2/blob/master/.travis.yml)
for details of the commands that are run as part of the Travis-CI build of this
project. The minimum bar for all push requests is that the Travis-CI build must
pass. Contributors are also strongly encouraged to add new tests to cover any
new functionality introduced into the gem.

### Installing gem dependencies via Bundler

To install all gem dependencies for the active version of Ruby and for a given
gemfile, you'll need to run the `bundle` command, e.g.

```bash
BUNDLE_GEMFILE=Gemfile.rails3 bundle
```

### Running tests against all configurations (requires [rbenv](https://github.com/sstephenson/rbenv))

To run tests against all configurations specified in the Travis-CI configuration
file, run `script/test-all`:

```bash
script/test-all
```

This scripts requires that you have rbenv installed along with all required
versions of Ruby. Furthermore, you'll need to make sure that each version of
Ruby installed via rbenv has all the required gems available to it installed
using the `bundle` command.

### Running tests against a single configuration

To manually run the Travis-CI verification steps on your local machine, you can
use the following sequence of commands for Rails 3.2.x:

```bash
script/test -g Gemfile.rails3
```

To test against Rails 4.0.x, use:

```bash
script/test -g Gemfile.rails4
```

`script/test` takes care of running Bundler to update any gem dependencies,
setting up the database, running all tests and then performing a test build of
the gem in order to catch any syntax errors.

## Licence

`user_impersonate2` is released under the MIT licence.

