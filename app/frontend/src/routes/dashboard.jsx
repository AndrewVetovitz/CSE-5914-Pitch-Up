// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import Person from "@material-ui/icons/Person";
// import ContentPaste from "@material-ui/icons/ContentPaste";
import LibraryBooks from "@material-ui/icons/LibraryBooks";
// core components/views
import PitchAnalysisPage from "views/PitchAnalysis/PitchAnalysis.jsx";
import UserProfile from "views/UserProfile/UserProfile.jsx";
import PitchesPage from "views/Pitches/Pitches.jsx";
import RecordingPage from "views/Recording/Recording.jsx";
import Pitch from "views/Pitch/Pitch.jsx"

const dashboardRoutes = [
    {
        path: "/user",
        sidebarName: "User Profile",
        navbarName: "Profile",
        icon: Person,
        component: UserProfile
    },
    {
        path: "/pitches",
        sidebarName: "Pitches",
        navbarName: "Pitches",
        icon: "content_paste",
        component: PitchesPage
    },
    {
        path: "/recording",
        sidebarName: "Recording Studio",
        navbarName: "Recording Studio",
        icon: LibraryBooks,
        component: RecordingPage,
        invisible: true
    },
    {
        path: "/pitch_analysis",
        sidebarName: "Pitch Results",
        navbarName: "Pitch Results",
        icon: Dashboard,
        component: PitchAnalysisPage,
        invisible: true
    },
    {
        path: "/pitch",
        sidebarName: "Pitch",
        navbarName: "Pitch",
        component: Pitch,
        invisible: true
    },
    {
        path: "/",
        to: "/user",
        redirect: true,
        invisible: true
    }
];

export default dashboardRoutes;
