import './App.css';
import { useState } from 'react';


function App() {

    const doc = document.getElementById("data")
    var args
    if (doc !== null) {
        args = JSON.parse(document.getElementById("data").text)
    } else {
        args =
        {
            "getUser": 'user',
            "pArtists": ['Adele', 'Koethe', 'alt-J'],
            "trackArtist": 'Koethe',
            "trackName": 'There Was Time',
            "trackRelated": 'Hannah Telle',
            "trackCover": 'https://i.scdn.co/image/ab67616d0000b273d896d08718bbf50e1e644667',
            "trackAudio": 'https://p.scdn.co/mp3-preview/119e33c553b89623dbdf44edfe784a4fa83a8a42?cid=fa0e0be98ca24262bd904cdefd7b9806',
            "trackLyrics": 'https://genius.com/Koethe-there-was-time-lyrics',
        }
    }


    function GetArtists(args) {
        const pArtists = args.pArtists;

        const [artists, setArtists] = useState(pArtists);

        // Flash Messages for Adding, Deleting, and Saving Artists
        const [msg, setMsg] = useState('');


        // Add Artists to Saved Artists
        const [artistName, setNewArtists] = useState(""); // Initializing state variables for adding artists
        const addArtist = (e) => {
            const newArtists = [...artists, artistName];
            setArtists(newArtists);
            setMsg('Artist added!');
        }


        // Delete Artists from Saved Artists
        const deleteArtist = (delIndex) => {
            const rmvArtists = [...artists].filter(artist => artist !== delIndex);
            setArtists(rmvArtists);
            setMsg('Artist deleted.');
        };


        // Update Saved Artists
        function SendFlask(appArtists) {
            //console.log(JSON.stringify({ "artists": appArtists }));
            setMsg('Saved artists list updated!');
            fetch('/appArtists', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ "artists": appArtists }),
            }).then(response => response.json()).then(data => {
                setArtists(data.appArtists_server);
                console.log(data.appArtists_server);
            });
        }


        return (
            <div className="addDelete">
                {artists.length !== 0 ? (
                    <>
                        <p style={{ padding: 0, margin: 0, fontSize: "16pt" }}>
                            {args.getUser}'s saved artists:
                        </p>
                        <nav>
                            <ul style={{ listStyleType: "none", paddingLeft: '0px', fontSize: "16pt" }}>
                                {artists.map(artist => (
                                    <li key={artist} style={{ listStyleType: "none", paddingLeft: '0px', display: 'flex', justifyContent: 'space-between', marginBottom: '5px' }}>
                                        {artist}
                                        <button className="artistDeleteButton" style={{ padding: '5px', borderRadius: '5px' }}
                                            onClick={() => deleteArtist(artist)} >
                                            Delete
                                        </button>
                                    </li>
                                ))}
                            </ul>
                        </nav>
                    </>) :
                    (<>
                        <p style={{ padding: 0, margin: 0, fontSize: "16pt", textAlign: 'center' }}>
                            Hi {args.getUser}, you currently have no artists saved. Please save an artist below.
                        </p>
                    </>)
                }
                <div style={{ display: 'flex', flexDirection: 'column', marginLeft: 'auto', marginRight: 'auto' }}>
                    <>
                        <input type="text" value={artistName} onChange={(e) => setNewArtists(e.target.value)} data-testid="Add-Button" placeholder="Name of Artist" />
                        <button onClick={addArtist}>Add artist</button>
                    </>
                    <>
                        <button className="artistSaveButton" style={{ marginLeft: 'auto', marginRight: 'auto', marginTop: '10px', marginBottom: '10px' }}
                            onClick={() => SendFlask(artists)} data-testid="Save-Button">
                            Save
                        </button>
                        <p className="flashes" style={{ color: '#69f0ae', fontSize: '12pt' }}>{msg}</p>
                    </>
                </div>
            </div>
        );
    }

    return (
        <>
            <h1>Britny's Jukebox</h1>
            <title>Britny's Jukebox</title>
            <div className="messageContainer">
                <div className="message">
                    {GetArtists(args)}
                </div>
            </div>

            <div className="trackContainer">
                <div className="trackArtistNameRelated">
                    <ul style={{ listStyleType: "none" }}>
                        <div className="trackArtist">
                            {args.trackArtist}
                        </div>
                        <div className="trackName">
                            {args.trackName}
                        </div>
                        <div className='trackRelated'>
                            Similar Artists:
                            <br></br>
                            {args.trackRelated}
                        </div>
                    </ul>
                </div>

                <div className="trackCoverAudioLyrics">
                    <ul style={{ listStyleType: "none", paddingLeft: "0px" }}>
                        <img src={args.trackCover} width="175px" height="175px"
                            style={{ borderRadius: "5px", marginLeft: "25%" }} alt="Album Cover Art"></img>
                        <audio src={args.trackAudio} controls style={{ padding: "10px" }}></audio>

                        <div className="trackLyrics">
                            <a href={args.trackLyrics}
                                className="lyricsURL">Click to see the lyrics!</a>
                        </div>
                    </ul>
                </div>
            </div >
        </>
    );


}
export default App;