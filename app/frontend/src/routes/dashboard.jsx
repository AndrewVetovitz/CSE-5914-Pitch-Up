// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import Person from "@material-ui/icons/Person";
// import ContentPaste from "@material-ui/icons/ContentPaste";
import LibraryBooks from "@material-ui/icons/LibraryBooks";
import BubbleChart from "@material-ui/icons/BubbleChart";
import LocationOn from "@material-ui/icons/LocationOn";
import Notifications from "@material-ui/icons/Notifications";
import Unarchive from "@material-ui/icons/Unarchive";
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
    component: RecordingPage
  },
  {
    path: "/pitch_analysis",
    sidebarName: "Pitch Results",
    navbarName: "Material Dashboard",
    icon: Dashboard,
    component: PitchAnalysisPage
  },
  {path:"/pitch", component: Pitch, invisible: true}
];

export default dashboardRoutes;
