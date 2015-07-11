# File for holding configuration relative to the current KLF
# This could be dberised sometimes
from pytz import timezone
from datetime import datetime
import os


klf_info = {
  'password_salt' : 'rojkadMeedmefMiopNis',
  'password_iterations' : 400000,

  'paymentgateway_userid' : '',
  'paymentgateway_secretkey' : '',

# Contact email for the committee
  'contact_email' : 'contact@klf2016.kansaslinuxfest.us',
# All email sent by ZK will Bcc here:
  'bcc_email' : 'archive@klf2016.kansaslinuxfest.us',
  'webmaster_email': 'webmaster@klf2016.kansaslinuxfest.us',

# Event information
  'event_parent_organisation' : 'Free/Libre Open Source and Open Knowledge Association of Kansas',
  'event_parent_url' : 'http://www.openkansas.us/',
  'event_generic_name' : 'kansaslinuxfest.us',
  'event_name' : 'kansaslinuxfest.us 2016',
  'event_shortname' : 'klf2016',
  'event_city' : 'Lawrence',
  'event_host' : 'klf2016.kansaslinuxfest.us',
  'event_url' : 'http://klf2016.kansaslinuxfest.us',
  'event_permalink' : 'http://klf2016.kansaslinuxfest.us',
  'event_hashtag' : '#KLF2016',
  'event_tax_number' : 'ABN 56 987 117 479',
    'event_postal_address' : '2527 Belle Crest Drive, Lawrence KS',
  'event_fax_number' : '',
    'event_phone_number': '+1 (908) 989-0434',
    'event_byline': 'kansaslinuxfest.us 2016 | 19 - 20 March | Follow the Flow',
  'event_pricing_disclaimer': 'All prices are in US dollars.',
    'event_trademark_notice': 'Linux is a registered trademark of Linus Torvalds',
    'event_airport_code': 'MCI',
    'date' : datetime(2016, 3, 19, 9, 0, 00),
  'media_license_name' : 'Creative Commons Attribution-Share Alike License',
  'media_license_url'  : 'http://creativecommons.org/licenses/by-sa/4.0/',
  'sales_tax_divisor'    : 1,
  'time_zone'   : timezone('America/Chicago'),

  'invoice_message' : 'Tickets are free.',

# Possible statuses not_open|open|closed
  'cfp_status' : 'closed',
  'cfmini_status' : 'closed',
  'proposal_editing' : 'open',
  'funding_status' : 'not_open',
  'funding_editing' : 'not_open',
  'conference_status': 'open',
  'account_creation': True,
# Mode
  'cfp_hide_assistance_info': 'no',
  'cfp_hide_assistance_options' : 'no',
  'cfp_hide_scores': 'no',

  'cfp_miniconf_list' : ["(none)", "Sysadmin", "Business", "Haecksen"],

  'sponsors': {
    'top': [
      {'alt': 'klf2015', 'src': '/images/history/klf2015-logo.png', 'href': 'http://klf2015.kansaslinuxfest.us/'},
    ],
    'slideshow': [
      {'alt': 'klf2015', 'src': '/images/history/klf2015-logo.png', 'href': 'http://klf2015.kansaslinuxfest.us/'},
    ],
  },

  'proposal_update_email': 'archive@klf2016.kansaslinuxfest.us', # recieve notifications when proposals are changed. Leave blank for none.
  'google_map_url': 'https://www.google.com/maps/@38.9604209,-95.253652,17z',
  'google_map_latlng': '38.9604209,-95.253652',
# mailing lists
  'mailing_list_announce_url': 'http://lists.kansaslinuxfest.us/listinfo/klf-announce',
  'mailing_list_announce_addr': 'klf-announce@kansaslinuxfest.us',
  'mailing_list_chat_url': 'http://lists.klf2016.kansaslinuxfest.us/klf2016-chat',
  'mailing_list_chat_addr': 'klf2016-chat@lists.klf2016.kansaslinuxfest.us',
  'zk_enabled_theme': 'zkpylons',

    'ogg_path':           'http://mirror.kansaslinuxfest.us/klf10/videos/ogg',
    'speex_path':         'http://mirror.kansaslinuxfest.us/klf10/videos/speex',
}

klf_rego = {
  'personal_info' : {
      'phone' : 'yes',
      'home_address' : 'yes',
  },

  # Set to yes to collect PGP key IDs in rego, no to disable collection.
  'pgp_collection': 'yes',

  # Set to no once the conference starts to speed things up
  'confirm_email_address' : 'yes',

  'ask_past_confs' : 'yes',
  'klf_optional_stuff' : 'yes',

  'volunteer':
    (
        {'title': 'Volunteer Category', 'questions':
            (
                {'name': 'Student Volunteer', 'description': 'I am eligible to attend as a Student and am willing to donate 100% of my time to the conference. I understand that I will be able to attend for free.'},
                {'name': 'Hobbyist Volunteer', 'description': 'I am eligible to attend as a Hobbyist and am willing to donate at least 50% of my time to the conference. I understand that I will be able to attend for the price of a student admission. (If you are happy to donate more than 50% of your time, please indicate a percentage in the "Other:" section.)'},
                {'name': 'Other Volunteer', 'description': 'I do not fit into the categories above or want to volunteer for a specific project or for less than the percentages above. Please provide details in the "Other:" section.'},
            )
        },
        {'title': 'Availability', 'questions':
            (
                {'name': 'Setup', 'description': 'I am available on the weekend prior to the conference (22 - 23 January) to help with setup.'},
                {'name': 'Sunday Registrations', 'description': 'I am available on the afternoon of Sunday 23 January to assist with pre-conference registrations.'},
                {'name': 'Conference', 'description': 'I am available for the full week of the conference (24 - 28 January).'},
                {'name': 'Pack up', 'description': 'I am available on the evening of Friday 28 January and Saturday 29 January to pack-up the conference.'},
                {'name': 'Other Dates', 'description': 'Please provide details in the "Other:" section.'},
            )
        },
        {'title': 'I am able and willing to help with ...', 'questions':
            (
                {'name': 'Speaker Introductions', 'description': 'Leading A/V and Ushers in a room, introducing speakers, keeping them to schedule, public announcements, etc.'},
                {'name': 'A/V', 'description': 'Filming in a lecture theatre. Training will be provided.'},
                {'name': 'Usher', 'description': 'Helping manage rooms, get people to seats, etc.'},
                {'name': 'Registration Desk', 'description': 'Sign people into the conference and help with general enquiries.'},
                {'name': 'Venue Helper', 'description': 'Help with setting up break times, tables and chairs, and other miscellaneous things.'},
                {'name': 'Other', 'description': 'Please provide details in the "Other:" section.'},
            ),
        }
    ),
  'shells' : ['bash', 'busybox', 'csh', 'dash', 'emacs', 'ksh', 'sh', 'smrsh', 'tcsh', 'XTree Gold', 'zsh'],
  'editors' : ['bluefish', 'eclipse', 'emacs', 'gedit', 'jed', 'kate', 'nano', 'vi', 'vim', 'xemacs'],
  'distros' : ['Arch', 'Arch/Hurd', 'CentOS', 'Darwin', 'Debian', 'Fedora', 'FreeBSD', 'FreeDOS', 'Gentoo', 'Hurd', 'GNU Emacs','Haiku OS','kFreeBSD','L4', 'Mandriva', 'Minix', 'MeeGo', 'NetBSD', 'Nexenta', 'OpenBSD', 'OpenSolaris', 'OpenSuSE', 'SLES','Oracle Enterprise Linux', 'RHEL', 'Slackware', 'Ubuntu', 'Xandros'],
  'vcses' : ['.bak', 'arch', 'bazaar', 'bitkeeper', 'cvs', 'darcs', 'git', 'mercurial', 'monotone', 'perforce', 'rcs', 'sourcesafe', 'subversion'],
  'past_confs' : [('15', '2015 (Lawrence)'), ('16', '2016 (TBA)')],

  'silly_description' : {
        'starts' : ["a", "a", "a", "one", "no"], # bias toward "a"
        'adverbs' : ["strongly",
               "poorly", "badly", "well", "dynamically",
               "hastily", "statically", "mysteriously",
               "buggily", "extremely", "nicely", "strangely",
               "irritatingly", "unquestionably", "clearly",
               "plainly", "silently", "abstractly", "validly",
               "invalidly", "immutably", "oddly", "disturbingly",
               "atonally", "randomly", "amusingly", "widely",
               "narrowly", "manually", "automatically", "audibly",
               "brilliantly", "independently", "definitively",
               "provably", "improbably", "distortingly",
               "confusingly", "decidedly", "historically",
               "shiny", "troublesome"],
        'adjectives' : ["invalid", "valid",
               "referenced", "dereferenced", "unreferenced",
               "illegal", "legal",
               "questionable",
               "alternate", "implemented", "unimplemented",
               "terminal", "non-terminal",
               "static", "dynamic",
               "qualified", "unqualified",
               "constant", "variable",
               "volatile", "non-volatile",
               "abstract", "concrete",
               "fungible", "non-fungible",
               "untyped", "variable",
               "mutable", "immutable",
               "sizable", "minuscule",
               "perverse", "immovable",
               "compressed", "uncompressed",
               "surreal", "allegorical",
               "trivial", "nontrivial"],
        'nouns' : ["pointer", "structure",
               "definition", "declaration", "type", "union",
               "coder", "admin", "hacker", "kitten", "mistake",
               "conversion", "implementation", "design", "analysis",
               "neophyte", "expert", "bundle", "package",
               "abstraction", "theorem", "display", "distro",
               "restriction", "device", "function", "reference",
               "alien"]
    }
}

klf_menu = [
  ('Home', '/', 'home'),
  ('About', '/about/kansaslinuxfest.us', 'about'),

    ('Location', '/location/about', 'location'),
#    ('Topeka', '/topeka/about', 'topeka'),
#    ('Lawrence', '/lawrence/about', 'lawrence'),
#    ('Manhatten', '/manhatten/about', 'manhatten'),
#    ('Wichita', '/wichita/about', 'wichita'),
#    ('Lenexa', '/lenexa/about', 'lenexa'),

    
  ('Sponsors', '/sponsors/sponsors', 'sponsors'),
  ('Programme', '/program/about', 'program'),
  ('Register', '/register/prices', 'register'),
  #('Register', '/register/prices', 'register'), # -- Stage 4
  ('Media', '/media/news', 'media'),
  ('Contact', '/contact', 'contact'),
  #('Planet', 'http://planet.klf2016.kansaslinuxfest.us', 'planet'),
  ('Wiki', '/wiki', 'wiki'),
]

klf_submenus = {
  'about': ['kansaslinuxfest.us', 'klf2016 Ninjas', 'Venue', 'History', 'Linux/Open Source', 'Harassment'],
  'location': ['About', 'Sightseeing'],
  'sponsors': ['Sponsors', 'Why Sponsor'],
  #'programme': ['About', 'Social Events', 'Open Day', 'Partners Programme'], # stage 0
  #'programme': ['About', 'Papers', 'Miniconfs', 'Presentations', 'Posters', 'Tutorials'], # stage 1
  #'programme': ['About', 'Keynotes', 'Miniconf Info', 'Papers Info', 'Social Events', 'Open Day', 'Partners Programme'], # stage 2
  #'programme': ['About', 'Keynotes', 'Miniconfs', 'Speakers Info', 'Social Events', 'Open Day', 'Partners Programme'], # stage 2a
  'programme': ['About', 'Keynotes', 'Miniconfs', 'Schedule', 'Social Events', 'Open Day', 'Partners Programme'], # stage 3
  #'programme': ['About', 'Keynotes', 'Miniconfs','Schedule','Social Events','Open Day', 'Partners Programme'], # stage 4?
  'register': ['Prices', 'Accommodation', 'Terms and Conditions'],
  #'register': ['Prices', 'Funding', 'Accommodation', 'Terms and Conditions'],
  #'register': ['Prices/Ticket types','Terms and Conditions','Accommodation','Partners programme'], # stage 4
  'media': ['News','In the press','Graphics']
}

