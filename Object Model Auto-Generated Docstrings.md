### Album Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for album
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		album_type (str): The type of the album: one of ``"album"`` ,
			``"single"`` , or ``"compilation"``.
		artists (array of simplified artist objects): The artists of the
			album.  Each artist object includes a link in ``href`` to more
			detailed information about the artist.
		available_markets (array of strings): The markets in which the
			album is available: ISO 3166-1 alpha-2 country codes.  Note
			that an album is considered available in a market when at least
			1 of its tracks is available in that market.
		copyrights (array of copyright objects): The copyright
			statements of the album.
		external_ids (an external ID object): Known external IDs for the
			album.
		external_urls (an external URL object): Known external URLs for
			this album.
		genres (array of strings): A list of the genres used to classify
			the album.  For example: ``"Prog Rock"`` , ``"Post-Grunge"``.
			(If not yet classified, the array is empty.)
		href (str): A link to the Web API endpoint providing full
			details of the album.
		id (str): The Spotify ID for the album.
		images (array of image objects): The cover art for the album in
			various sizes, widest first.
		label (str): The label for the album.
		name (str): The name of the album.  In case of an album
			takedown, the value may be an empty string.
		popularity (int): The popularity of the album.  The value will
			be between 0 and 100, with 100 being the most popular.  The
			popularity is calculated from the popularity of the albums
			individual tracks.
		release_date (str): The date the album was first released, for
			example ``1981``. Depending on the precision, it might be shown
			as ``1981-12`` or ``1981-12-15``.
		release_date_precision (str): The precision with which
			``release_date`` value is known: ``year`` , ``month`` , or
			``day``.
		restrictions (a restrictions object): Part of the response when
			Track Relinking is applied, the original track is not available
			in the given market, and Spotify did not have any tracks to
			relink it with.  The track response will still contain metadata
			for the original track, and a restrictions object containing
			the reason why the track is not available: ``"restrictions" :
			{"reason" : "market"}``
		tracks (array of simplified track objects inside a paging
			object): The tracks of the album.
		type (str): The object type: album
		uri (str): The Spotify URI for the album.
	"""
```

### Album Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for album
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		album_group (string, optional): The field is present when
			getting an artists albums.  Possible values are album, single,
			compilation, appears_on.  Compare to album_type this field
			represents relationship between the artist and the album.
		album_type (str): The type of the album: one of album, single,
			or compilation.
		artists (array of simplified artist objects): The artists of the
			album.  Each artist object includes a link in ``href`` to more
			detailed information about the artist.
		available_markets (array of strings): The markets in which the
			album is available: ISO 3166-1 alpha-2 country codes.  Note
			that an album is considered available in a market when at least
			1 of its tracks is available in that market.
		external_urls (an external URL object): Known external URLs for
			this album.
		href (str): A link to the Web API endpoint providing full
			details of the album.
		id (str): The Spotify ID for the album.
		images (array of image objects): The cover art for the album in
			various sizes, widest first.
		name (str): The name of the album.  In case of an album
			takedown, the value may be an empty string.
		release_date (str): The date the album was first released, for
			example ``1981``. Depending on the precision, it might be shown
			as ``1981-12`` or ``1981-12-15``.
		release_date_precision (str): The precision with which
			``release_date`` value is known: ``year`` , ``month`` , or
			``day``.
		restrictions (a restrictions object): Part of the response when
			Track Relinking is applied, the original track is not available
			in the given market, and Spotify did not have any tracks to
			relink it with.  The track response will still contain metadata
			for the original track, and a restrictions object containing
			the reason why the track is not available: ``"restrictions" :
			{"reason" : "market"}``
		type (str): The object type: album
		uri (str): The Spotify URI for the album.
	"""
```

### Artist Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for artist
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		external_urls (an external URL object): Known external URLs for
			this artist.
		followers (A followers object): Information about the followers
			of the artist.
		genres (array of strings): A list of the genres the artist is
			associated with.  For example: ``"Prog Rock"`` , ``"Post-
			Grunge"``. (If not yet classified, the array is empty.)
		href (str): A link to the Web API endpoint providing full
			details of the artist.
		id (str): The Spotify ID for the artist.
		images (array of image objects): Images of the artist in various
			sizes, widest first.
		name (str): The name of the artist.
		popularity (int): The popularity of the artist.  The value will
			be between 0 and 100, with 100 being the most popular.  The
			artists popularity is calculated from the popularity of all the
			artists tracks.
		type (str): The object type: ``"artist"``
		uri (str): The Spotify URI for the artist.
	"""
```

### Artist Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for artist
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		external_urls (an external URL object): Known external URLs for
			this artist.
		href (str): A link to the Web API endpoint providing full
			details of the artist.
		id (str): The Spotify ID for the artist.
		name (str): The name of the artist.
		type (str): The object type: ``"artist"``
		uri (str): The Spotify URI for the artist.
	"""
```

### Audio Features Object
```python
	"""Auto-generated attribute instantiation docstring for audio
	features object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		acousticness (float): A confidence measure from 0.0 to 1.0 of
			whether the track is acoustic.  1.0 represents high confidence
			the track is acoustic.
		analysis_url (str): An HTTP URL to access the full audio
			analysis of this track.  An access token is required to access
			this data.
		danceability (float): Danceability describes how suitable a
			track is for dancing based on a combination of musical elements
			including tempo, rhythm stability, beat strength, and overall
			regularity.  A value of 0.0 is least danceable and 1.0 is most
			danceable.
		duration_ms (int): The duration of the track in milliseconds.
		energy (float): Energy is a measure from 0.0 to 1.0 and
			represents a perceptual measure of intensity and activity.
			Typically, energetic tracks feel fast, loud, and noisy.  For
			example, death metal has high energy, while a Bach prelude
			scores low on the scale.  Perceptual features contributing to
			this attribute include dynamic range, perceived loudness,
			timbre, onset rate, and general entropy.
		id (str): The Spotify ID for the track.
		instrumentalness (float): Predicts whether a track contains no
			vocals.  Ooh and aah sounds are treated as instrumental in this
			context.  Rap or spoken word tracks are clearly vocal.  The
			closer the instrumentalness value is to 1.0, the greater
			likelihood the track contains no vocal content.  Values above
			0.5 are intended to represent instrumental tracks, but
			confidence is higher as the value approaches 1.0.
		key (int): The key the track is in.  Integers map to pitches
			using standard Pitch Class notation.  E.g.  0 = C, 1 = C/D, 2 =
			D, and so on.
		liveness (float): Detects the presence of an audience in the
			recording.  Higher liveness values represent an increased
			probability that the track was performed live.  A value above
			0.8 provides strong likelihood that the track is live.
		loudness (float): The overall loudness of a track in decibels
			(dB). Loudness values are averaged across the entire track and
			are useful for comparing relative loudness of tracks.  Loudness
			is the quality of a sound that is the primary psychological
			correlate of physical strength (amplitude). Values typical
			range between -60 and 0 db.
		mode (int): Mode indicates the modality (major or minor) of a
			track, the type of scale from which its melodic content is
			derived.  Major is represented by 1 and minor is 0.
		speechiness (float): Speechiness detects the presence of spoken
			words in a track.  The more exclusively speech-like the
			recording (e.g.  talk show, audio book, poetry), the closer to
			1.0 the attribute value.  Values above 0.66 describe tracks
			that are probably made entirely of spoken words.  Values
			between 0.33 and 0.66 describe tracks that may contain both
			music and speech, either in sections or layered, including such
			cases as rap music.  Values below 0.33 most likely represent
			music and other non-speech-like tracks.
		tempo (float): The overall estimated tempo of a track in beats
			per minute (BPM). In musical terminology, tempo is the speed or
			pace of a given piece and derives directly from the average
			beat duration.
		time_signature (int): An estimated overall time signature of a
			track.  The time signature (meter) is a notational convention
			to specify how many beats are in each bar (or measure).
		track_href (str): A link to the Web API endpoint providing full
			details of the track.
		type (str): The object type: audio_features
		uri (str): The Spotify URI for the track.
		valence (float): A measure from 0.0 to 1.0 describing the
			musical positiveness conveyed by a track.  Tracks with high
			valence sound more positive (e.g.  happy, cheerful, euphoric),
			while tracks with low valence sound more negative (e.g.  sad,
			depressed, angry).
	"""
```

### Category Object
```python
	"""Auto-generated attribute instantiation docstring for category
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		href (str): A link to the Web API endpoint returning full
			details of the category.
		icons (an array of image objects): The category icon, in various
			sizes.
		id (str): The Spotify category ID of the category.
		name (str): The name of the category.
	"""
```

### Context Object
```python
	"""Auto-generated attribute instantiation docstring for context
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		type (str): The object type, e.g.  artist, playlist, album.
		href (str): A link to the Web API endpoint providing full
			details of the track.
		external_urls (an external URL object): External URLs for this
			context.
		uri (str): The Spotify URI for the context.
	"""
```

### Copyright Object
```python
	"""Auto-generated attribute instantiation docstring for copyright
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		text (str): The copyright text for this album.
		type (str): The type of copyright: ``C`` = the copyright, ``P``
			= the sound recording (performance) copyright.
	"""
```

### Cursor Object
```python
	"""Auto-generated attribute instantiation docstring for cursor
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		after (str): The cursor to use as key to find the next page of
			items.
	"""
```

### Error Object
```python
	"""Auto-generated attribute instantiation docstring for error
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		status (int): The HTTP status code (also returned in the
			response header; see Response Status Codes for more
			information).
		message (str): A short description of the cause of the error.
	"""
```

### Player Error Reasons
```python
	"""Auto-generated attribute instantiation docstring for player
	error reasons

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		403 FORBIDDEN (UNKNOWN): Certain actions are restricted because
			of unknown reasons.
		404 NOT FOUND (NO_ACTIVE_DEVICE): Requires an active device and
			the user has none.
	"""
```

### External Id Object
```python
	"""Auto-generated attribute instantiation docstring for external
	ID object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		{key} (str): The identifier type, for example:- ``"isrc"`` -
			International Standard Recording Code- ``"ean"`` -
			International Article Number- ``"upc"`` - Universal Product
			Code
		{value} (str): An external identifier for the object.
	"""
```

### External Url Object
```python
	"""Auto-generated attribute instantiation docstring for external
	URL object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		{key} (str): The type of the URL, for example:- ``"spotify"`` -
			The Spotify URL for the object.
		{value} (str): An external, public URL to the object.
	"""
```

### Followers Object
```python
	"""Auto-generated attribute instantiation docstring for followers
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		href (str): A link to the Web API endpoint providing full
			details of the followers; ``null`` if not available.  Please
			note that this will always be set to null, as the Web API does
			not support it at the moment.
		total (int): The total number of followers.
	"""
```

### Image Object
```python
	"""Auto-generated attribute instantiation docstring for image
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		height (int): The image height in pixels.  If unknown: ``null``
			or not returned.
		url (str): The source URL of the image.
		width (int): The image width in pixels.  If unknown: ``null`` or
			not returned.
	"""
```

### Paging Object
```python
	"""Auto-generated attribute instantiation docstring for paging
	object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		href (str): A link to the Web API endpoint returning the full
			result of the request.
		items (an array of objects): The requested data.
		limit (int): The maximum number of items in the response (as set
			in the query or by default).
		next (str): URL to the next page of items.  ( ``null`` if none)
		offset (int): The offset of the items returned (as set in the
			query or by default).
		previous (str): URL to the previous page of items.  ( ``null``
			if none)
		total (int): The maximum number of items available to return.
	"""
```

### Cursor-Based Paging Object
```python
	"""Auto-generated attribute instantiation docstring for cursor-
	based paging object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		href (str): A link to the Web API endpoint returning the full
			result of the request.
		items (an array of objects): The requested data.
		limit (int): The maximum number of items in the response (as set
			in the query or by default).
		next (str): URL to the next page of items.  ( ``null`` if none)
		cursors (cursor object): The cursors used to find the next set
			of items.
		total (int): The maximum number of items available to return.
	"""
```

### Play History Object
```python
	"""Auto-generated attribute instantiation docstring for play
	history object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		track (track object(simplified)): The track the user listened
			to.
		played_at (timestamp): The date and time the track was played.
		context (context object): The context the track was played from.
	"""
```

### Playlist Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for playlist
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		collaborative (Boolean): Returns ``true`` if context is not
			search and the owner allows other users to modify the playlist.
			Otherwise returns ``false``.
		description (str): The playlist description.  Only returned for
			modified, verified playlists, otherwise ``null``.
		external_urls (an external URL object): Known external URLs for
			this playlist.
		followers (a followers object): Information about the followers
			of the playlist.
		href (str): A link to the Web API endpoint providing full
			details of the playlist.
		id (str): The Spotify ID for the playlist.
		images (an array of image objects): Images for the playlist.
			The array may be empty or contain up to three images.  The
			images are returned by size in descending order.  See Working
			with Playlists.Note: If returned, the source URL for the image
			( ``url`` ) is temporary and will expire in less than a day.
		name (str): The name of the playlist.
		owner (a public user object): The user who owns the playlist
		public (Boolean or null): The playlists public/private status:
			``true`` the playlist is public, ``false`` the playlist is
			private, ``null`` the playlist status is not relevant.  For
			more about public/private status, see Working with Playlists.
		snapshot_id (str): The version identifier for the current
			playlist.  Can be supplied in other requests to target a
			specific playlist version: see Remove tracks from a playlist
		tracks (array of playlist track objects inside a paging object):
			Information about the tracks of the playlist.
		type (str): The object type: playlist
		uri (str): The Spotify URI for the playlist.
	"""
```

### Playlist Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for playlist
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		collaborative (Boolean): Returns ``true`` if context is not
			search and the owner allows other users to modify the playlist.
			Otherwise returns ``false``.
		description (str): The playlist description.  Only returned for
			modified, verified playlists, otherwise ``null`` .
		external_urls (an external URL object): Known external URLs for
			this playlist.
		href (str): A link to the Web API endpoint providing full
			details of the playlist.
		id (str): The Spotify ID for the playlist.
		images (an array of image objects): Images for the playlist.
			The array may be empty or contain up to three images.  The
			images are returned by size in descending order.  See Working
			with Playlists.Note: If returned, the source URL for the image
			( ``url`` ) is temporary and will expire in less than a day.
		name (str): The name of the playlist.
		owner (a user object): The user who owns the playlist
		public (Boolean or null): The playlists public/private status:
			``true`` the playlist is public, ``false`` the playlist is
			private, ``null`` the playlist status is not relevant.  For
			more about public/private status, see Working with Playlists.
		snapshot_id (str): The version identifier for the current
			playlist.  Can be supplied in other requests to target a
			specific playlist version
		tracks (array of playlist track objects inside a paging object):
			Information about the tracks of the playlist.
		type (str): The object type: playlist
		uri (str): The Spotify URI for the playlist.
	"""
```

### Playlist Track Object
```python
	"""Auto-generated attribute instantiation docstring for playlist
	track object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		added_at (a timestamp): The date and time the track or episode
			was added.Note that some very old playlists may return ``null``
			in this field.
		added_by (a user object): The Spotify user who added the track
			or episode.Note that some very old playlists may return
			``null`` in this field.
		is_local (a Boolean): Whether this track or episode is a local
			file or not.
		track (a track object or a episode object): Information about
			the track or episode.
	"""
```

### Recommendations Object
```python
	"""Auto-generated attribute instantiation docstring for
	recommendations object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		seeds (array): An array of recommendation seed objects.
		tracks (array): An array of track object (simplified) ordered
			according to the parameters supplied.
	"""
```

### Recommendations Seed Object
```python
	"""Auto-generated attribute instantiation docstring for
	recommendations seed object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		afterFilteringSize (int): The number of tracks available after
			min_* and max_* filters have been applied.
		afterRelinkingSize (int): The number of tracks available after
			relinking for regional availability.
		href (str): A link to the full track or artist data for this
			seed.  For tracks this will be a link to a Track Object.  For
			artists a link to an Artist Object.  For genre seeds, this
			value will be ``null``.
		id (str): The id used to select this seed.  This will be the
			same as the string used in the ``seed_artists`` ,
			``seed_tracks`` or ``seed_genres`` parameter.
		initialPoolSize (int): The number of recommended tracks
			available for this seed.
		type (str): The entity type of this seed.  One of ``artist`` ,
			``track`` or ``genre``.
	"""
```

### Saved Track Object
```python
	"""Auto-generated attribute instantiation docstring for saved
	track object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		added_at (a timestamp): The date and time the track was saved.
		track (a track object): Information about the track.
	"""
```

### Saved Album Object
```python
	"""Auto-generated attribute instantiation docstring for saved
	album object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		added_at (a timestamp): The date and time the album was saved.
		album (an album object): Information about the album.
	"""
```

### Saved Show Object
```python
	"""Auto-generated attribute instantiation docstring for saved
	show object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		added_at (a timestamp): The date and time the show was saved.
		show (a show object): Information about the show.
	"""
```

### Track Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for track
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		album (a simplified album object): The album on which the track
			appears.  The album object includes a link in ``href`` to full
			information about the album.
		artists (an array of simplified artist objects): The artists who
			performed the track.  Each artist object includes a link in
			``href`` to more detailed information about the artist.
		available_markets (array of strings): A list of the countries in
			which the track can be played, identified by their ISO 3166-1
			alpha-2 code.
		disc_number (int): The disc number (usually ``1`` unless the
			album consists of more than one disc).
		duration_ms (int): The track length in milliseconds.
		explicit (Boolean): Whether or not the track has explicit lyrics
			( ``true`` = yes it does; ``false`` = no it does not OR
			unknown).
		external_ids (an external ID object): Known external IDs for the
			track.
		external_urls (an external URL object): Known external URLs for
			this track.
		href (str): A link to the Web API endpoint providing full
			details of the track.
		id (str): The Spotify ID for the track.
		is_playable (bool): Part of the response when Track Relinking is
			applied.  If ``true`` , the track is playable in the given
			market.  Otherwise ``false``.
		linked_from (a linked track object): Part of the response when
			Track Relinking is applied, and the requested track has been
			replaced with different track.  The track in the
			``linked_from`` object contains information about the
			originally requested track.
		restrictions (a restrictions object): Part of the response when
			Track Relinking is applied, the original track is not available
			in the given market, and Spotify did not have any tracks to
			relink it with.  The track response will still contain metadata
			for the original track, and a restrictions object containing
			the reason why the track is not available: ``"restrictions" :
			{"reason" : "market"}``
		name (str): The name of the track.
		popularity (int): The popularity of the track.  The value will
			be between 0 and 100, with 100 being the most popular.The
			popularity of a track is a value between 0 and 100, with 100
			being the most popular.  The popularity is calculated by
			algorithm and is based, in the most part, on the total number
			of plays the track has had and how recent those plays
			are.Generally speaking, songs that are being played a lot now
			will have a higher popularity than songs that were played a lot
			in the past.  Duplicate tracks (e.g.  the same track from a
			single and an album) are rated independently.  Artist and album
			popularity is derived mathematically from track popularity.
			Note that the popularity value may lag actual popularity by a
			few days: the value is not updated in real time.
		preview_url (str): A link to a 30 second preview (MP3 format) of
			the track.  Can be ``null``
		track_number (int): The number of the track.  If an album has
			several discs, the track number is the number on the specified
			disc.
		type (str): The object type: track.
		uri (str): The Spotify URI for the track.
		is_local (bool): Whether or not the track is from a local file.
	"""
```

### Track Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for track
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		artists (an array of simple artist objects): The artists who
			performed the track.  Each artist object includes a link in
			``href`` to more detailed information about the artist.
		available_markets (array of strings): A list of the countries in
			which the track can be played, identified by their ISO 3166-1
			alpha-2 code.
		disc_number (int): The disc number (usually ``1`` unless the
			album consists of more than one disc).
		duration_ms (int): The track length in milliseconds.
		explicit (Boolean): Whether or not the track has explicit lyrics
			( ``true`` = yes it does; ``false`` = no it does not OR
			unknown).
		external_urls (an external URL object): External URLs for this
			track.
		href (str): A link to the Web API endpoint providing full
			details of the track.
		id (str): The Spotify ID for the track.
		is_playable (bool): Part of the response when Track Relinking is
			applied.  If ``true`` , the track is playable in the given
			market.  Otherwise ``false``.
		linked_from (a linked track object): Part of the response when
			Track Relinking is applied and is only part of the response if
			the track linking, in fact, exists.  The requested track has
			been replaced with a different track.  The track in the
			``linked_from`` object contains information about the
			originally requested track.
		restrictions (a restrictions object): Part of the response when
			Track Relinking is applied, the original track is not available
			in the given market, and Spotify did not have any tracks to
			relink it with.  The track response will still contain metadata
			for the original track, and a restrictions object containing
			the reason why the track is not available: ``"restrictions" :
			{"reason" : "market"}``
		name (str): The name of the track.
		preview_url (str): A URL to a 30 second preview (MP3 format) of
			the track.
		track_number (int): The number of the track.  If an album has
			several discs, the track number is the number on the specified
			disc.
		type (str): The object type: track.
		uri (str): The Spotify URI for the track.
		is_local (bool): Whether or not the track is from a local file.
	"""
```

### Track Link
```python
	"""Auto-generated attribute instantiation docstring for track
	link

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		external_urls (an external URL object): Known external URLs for
			this track.
		href (str): A link to the Web API endpoint providing full
			details of the track.
		id (str): The Spotify ID for the track.
		type (str): The object type: track.
		uri (str): The Spotify URI for the track.
	"""
```

### Episode Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for episode
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		audio_preview_url (str): A URL to a 30 second preview (MP3
			format) of the episode.  ``null`` if not available.
		description (str): A description of the episode.
		duration_ms (int): The episode length in milliseconds.
		explicit (bool): Whether or not the episode has explicit content
			(true = yes it does; false = no it does not OR unknown).
		external_urls (an external URL object): External URLs for this
			episode.
		href (str): A link to the Web API endpoint providing full
			details of the episode.
		id (str): The Spotify ID for the episode.
		images (array of image objects): The cover art for the episode
			in various sizes, widest first.
		is_externally_hosted (bool): True if the episode is hosted
			outside of Spotifys CDN.
		is_playable (bool): True if the episode is playable in the given
			market.  Otherwise false.
		language (str): Note: This field is deprecated and might be
			removed in the future.  Please use the ``languages`` field
			instead.  The language used in the episode, identified by a ISO
			639 code.
		languages (array of strings): A list of the languages used in
			the episode, identified by their ISO 639 code.
		name (str): The name of the episode.
		release_date (str): The date the episode was first released, for
			example ``"1981-12-15"``. Depending on the precision, it might
			be shown as ``"1981"`` or ``"1981-12"``.
		release_date_precision (str): The precision with which
			``release_date`` value is known: ``"year"``, ``"month"``, or
			``"day"``.
		resume_point (a resume point object): The users most recent
			position in the episode.  Set if the supplied access token is a
			user token and has the scope ``user-read-playback-position``.
		show (a simplified show object): The show on which the episode
			belongs.
		type (str): The object type: ``"episode"``.
		uri (str): The Spotify URI for the episode.
	"""
```

### Episode Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for episode
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		audio_preview_url (str): A URL to a 30 second preview (MP3
			format) of the episode.  ``null`` if not available.
		description (str): A description of the episode.
		duration_ms (int): The episode length in milliseconds.
		explicit (bool): Whether or not the episode has explicit content
			(true = yes it does; false = no it does not OR unknown).
		external_urls (an external URL object): External URLs for this
			episode.
		href (str): A link to the Web API endpoint providing full
			details of the episode.
		id (str): The Spotify ID for the episode.
		images (array of image objects): The cover art for the episode
			in various sizes, widest first.
		is_externally_hosted (bool): True if the episode is hosted
			outside of Spotifys CDN.
		is_playable (bool): True if the episode is playable in the given
			market.  Otherwise false.
		language (str): Note: This field is deprecated and might be
			removed in the future.  Please use the ``languages`` field
			instead.  The language used in the episode, identified by a ISO
			639 code.
		languages (array of strings): A list of the languages used in
			the episode, identified by their ISO 639 code.
		name (str): The name of the episode.
		release_date (str): The date the episode was first released, for
			example ``"1981-12-15"``. Depending on the precision, it might
			be shown as ``"1981"`` or ``"1981-12"``.
		release_date_precision (str): The precision with which
			``release_date`` value is known: ``"year"``, ``"month"``, or
			``"day"``.
		resume_point (a resume point object): The users most recent
			position in the episode.  Set if the supplied access token is a
			user token and has the scope ``user-read-playback-position``.
		type (str): The object type: ``"episode"``.
		uri (str): The Spotify URI for the episode.
	"""
```

### Resume Point Object
```python
	"""Auto-generated attribute instantiation docstring for resume
	point object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		fully_played (bool): Whether or not the episode has been fully
			played by the user.
		resume_position_ms (int): The users most recent position in the
			episode in milliseconds.
	"""
```

### Show Object (Full)
```python
	"""Auto-generated attribute instantiation docstring for show
	object (full)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		available_markets (array of strings): A list of the countries in
			which the show can be played, identified by their ISO 3166-1
			alpha-2 code.
		copyrights (array of copyright objects): The copyright
			statements of the show.
		description (str): A description of the show.
		explicit (bool): Whether or not the show has explicit content
			(true = yes it does; false = no it does not OR unknown).
		episodes (array of simplified episode objects inside a paging
			object.): A list of the shows episodes.
		external_urls (an external URL object): Known external URLs for
			this show.
		href (str): A link to the Web API endpoint providing full
			details of the show.
		id (str): The Spotify ID for the show.
		images (array of image objects): The cover art for the show in
			various sizes, widest first.
		is_externally_hosted (bool): True if all of the shows episodes
			are hosted outside of Spotifys CDN. This field might be
			``null`` in some cases.
		languages (array of strings): A list of the languages used in
			the show, identified by their ISO 639 code.
		media_type (str): The media type of the show.
		name (str): The name of the show.
		publisher (str): The publisher of the show.
		type (str): The object type: show.
		uri (str): The Spotify URI for the show.
	"""
```

### Show Object (Simplified)
```python
	"""Auto-generated attribute instantiation docstring for show
	object (simplified)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		available_markets (array of strings): A list of the countries in
			which the show can be played, identified by their ISO 3166-1
			alpha-2 code.
		copyrights (array of copyright objects): The copyright
			statements of the show.
		description (str): A description of the show.
		explicit (bool): Whether or not the show has explicit content
			(true = yes it does; false = no it does not OR unknown).
		external_urls (an external URL object): Known external URLs for
			this show.
		href (str): A link to the Web API endpoint providing full
			details of the show.
		id (str): The Spotify ID for the show.
		images (array of image objects): The cover art for the show in
			various sizes, widest first.
		is_externally_hosted (bool): True if all of the shows episodes
			are hosted outside of Spotifys CDN. This field might be
			``null`` in some cases.
		languages (array of strings): A list of the languages used in
			the show, identified by their ISO 639 code.
		media_type (str): The media type of the show.
		name (str): The name of the show.
		publisher (str): The publisher of the show.
		type (str): The object type: show.
		uri (str): The Spotify URI for the show.
	"""
```

### UserDBO Object (Private)
```python
	"""Auto-generated attribute instantiation docstring for user
	object (private)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		country (str): The country of the user, as set in the users
			account profile.  An ISO 3166-1 alpha-2 country code.  This
			field is only available when the current user has granted
			access to the user-read-private scope.
		display_name (str): The name displayed on the users profile.
			``null`` if not available.
		email (str): The users email address, as entered by the user
			when creating their account.Important!  This email address is
			unverified; there is no proof that it actually belongs to the
			user.This field is only available when the current user has
			granted access to the user-read-email scope.
		external_urls (an external URL object): Known external URLs for
			this user.
		followers (A followers object): Information about the followers
			of the user.
		href (str): A link to the Web API endpoint for this user.
		id (str): The Spotify user ID for the user
		images (an array of image objects): The users profile image.
		product (str): The users Spotify subscription level: premium,
			free, etc.  (The subscription level open can be considered the
			same as free.)This field is only available when the current
			user has granted access to the user-read-private scope.
		type (str): The object type: user
		uri (str): The Spotify URI for the user.
	"""
```

### UserDBO Object (Public)
```python
	"""Auto-generated attribute instantiation docstring for user
	object (public)

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		display_name (str): The name displayed on the users profile.
			``null`` if not available.
		external_urls (an external URL object): Known public external
			URLs for this user.
		followers (A followers object): Information about the followers
			of this user.
		href (str): A link to the Web API endpoint for this user.
		id (str): The Spotify user ID for this user.
		images (array of image objects): The users profile image.
		type (str): The object type: user
		uri (str): The Spotify URI for this user.
	"""
```

### Currently Playing Context
```python
	"""Auto-generated attribute instantiation docstring for Currently
	Playing Context

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		device (Device Object): The device that is currently active
		repeat_state (str): off, track, context
		shuffle_state (bool): If shuffle is on or off
		context (a Context Object): A Context Object.  Can be null (e.g.
			If private session is enabled this will be null).
		timestamp (int): Unix Millisecond Timestamp when data was
			fetched
		progress_ms (int): Progress into the currently playing track.
			Can be null (e.g.  If private session is enabled this will be
			null).
		is_playing (bool): If something is currently playing.
		item (A Full Track Object or A Full Episode Object): The
			currently playing track or episode.  Can be null (e.g.  If
			private session is enabled this will be null).
		currently_playing_type (str): The object type of the currently
			playing item.  Can be one of ``track``, ``episode``, ``ad`` or
			``unknown``.
		actions (An actions object which contains a disallows object):
			Allows to update the user interface based on which playback
			actions are available within the current context
	"""
```

### Device Object
```python
	"""Auto-generated attribute instantiation docstring for Device
	Object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		id (str): The device ID. This may be null.
		is_active (bool): If this device is the currently active device.
		is_private_session (bool): If this device is currently in a
			private session.
		is_restricted (bool): Whether controlling this device is
			restricted.  At present if this is true then no Web API
			commands will be accepted by this device.
		name (str): The name of the device.
		type (str): Device type, such as Computer, Smartphone or
			Speaker.
		volume_percent (int): The current volume in percent.  This may
			be null.
	"""
```

### Context Object
```python
	"""Auto-generated attribute instantiation docstring for Context
	Object

	Note: Parameter description in below docstring is populated based
	on the  descriptions at the following link:
	https://developer.spotify.com/documentation/web-
	api/reference/object-model

	Please consult their official documentation for more in-depth
	information & full-linking across pages.

	Attributes:
		uri (str): The uri of the context.
		href (str): The href of the context, or null if not available.
		external_urls (An External URL Object): The external_urls of the
			context, or null if not available.
		type (str): The object type of the items context.  Can be one of
			``album`` , ``artist`` or ``playlist``.
	"""
```